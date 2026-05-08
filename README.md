# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--08_13:19:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **146,201 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 13:19:22 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | -0.016 |  |
| 2026-05-08 13:17:21 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:11:59 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.037 |  |
| 2026-05-08 13:11:40 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-05-08 13:11:28 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-08 13:11:26 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-05-08 13:09:15 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 13:08:33 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.075 |  |
| 2026-05-08 13:07:14 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.195 |  |
| 2026-05-08 13:07:06 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.038 |  |
| 2026-05-08 13:06:40 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-05-08 13:05:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 13:05:25 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-08 13:05:19 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:05:12 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-08 13:05:08 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:04:50 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.057 |  |
| 2026-05-08 13:04:10 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-08 13:03:59 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 13:03:38 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-05-08 13:03:29 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.152 |  |
| 2026-05-08 13:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.078 |  |
| 2026-05-08 13:03:28 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.049 |  |
| 2026-05-08 13:02:44 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.052 |  |
| 2026-05-08 13:02:33 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:02:14 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.033 |  |
| 2026-05-08 13:02:10 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:02:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-05-08 13:01:53 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-05-08 13:01:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-08 13:01:23 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:01:17 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:01:08 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 13:01:03 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-05-08 13:00:30 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.021 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-08 13:05:44 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-05-08 13:04:10 | Moragaswewa (Deduru Oya) | 0.90 | 🟢 Normal | 0.055 | 🔺 Rising |
| 2026-05-08 13:01:08 | Thanthirimale (Malwathu Oya) | 1.92 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-05-08 13:05:12 | Dunamale (Aththanagalu Oya) | 1.08 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-08 13:03:59 | Norwood (Kelani Ganga) | 0.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-08 13:09:15 | Kithulgala (Kelani Ganga) | 1.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-08 13:11:28 | Horowpothana (Yan Oya) | 1.77 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-05-08 13:17:21 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:02:33 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:02:10 | Katharagama (Menik Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-08 12:01:20 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-05-08 11:10:09 | Rathnapura (Kalu Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-05-08 13:11:26 | Padiyathalawa (Maduru Oya) | 0.31 | 🟢 Normal | -0.009 |  |
| 2026-05-08 13:05:19 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:02:00 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:01:17 | Wellawaya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:02:09 | Deraniyagala (Kelani Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:00:30 | Moraketiya (Walawe Ganga) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-05-08 13:19:22 | Galgamuwa (Mee Oya) | 0.47 | 🟢 Normal | -0.016 |  |
| 2026-05-08 13:05:25 | Putupaula (Kalu Ganga) | 0.68 | 🟢 Normal | -0.019 |  |
| 2026-05-08 13:01:57 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.020 |  |
| 2026-05-08 13:06:40 | Baddegama (Gin Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-05-08 13:01:24 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.020 |  |
| 2026-05-08 13:00:11 | Weraganthota (Mahaweli Ganga) | -2.82 | 🟢 Normal | -0.021 |  |
| 2026-05-08 13:01:03 | Thalgahagoda (Nilwala Ganga) | 0.87 | 🟢 Normal | -0.021 |  |
| 2026-05-08 13:11:40 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.026 |  |
| 2026-05-08 13:02:14 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.033 |  |
| 2026-05-08 13:11:59 | Magura (Kalu Ganga) | 1.44 | 🟢 Normal | -0.037 |  |
| 2026-05-08 13:07:06 | Thawalama (Gin Ganga) | 1.68 | 🟢 Normal | -0.038 |  |
| 2026-05-08 13:01:53 | Kuda Oya (Kirindi Oya) | 1.81 | 🟢 Normal | -0.039 |  |
| 2026-05-08 12:05:23 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | -0.044 |  |
| 2026-05-08 13:03:28 | Badalgama (Maha Oya) | 3.04 | 🟢 Normal | -0.049 |  |
| 2026-05-08 13:02:44 | Thanamalwila (Kirindi Oya) | 1.85 | 🟢 Normal | -0.052 |  |
| 2026-05-08 13:04:50 | Ellagawa (Kalu Ganga) | 5.56 | 🟢 Normal | -0.057 |  |
| 2026-05-08 13:08:33 | Glencourse (Kelani Ganga) | 9.92 | 🟢 Normal | -0.075 |  |
| 2026-05-08 13:03:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.82 | 🟢 Normal | -0.078 |  |
| 2026-05-08 13:03:38 | Giriulla (Maha Oya) | 1.77 | 🟢 Normal | -0.080 |  |
| 2026-05-08 13:03:29 | Hanwella (Kelani Ganga) | 2.00 | 🟢 Normal | -0.152 |  |
| 2026-05-08 13:07:14 | Panadugama (Nilwala Ganga) | 3.98 | 🟢 Normal | -0.195 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)