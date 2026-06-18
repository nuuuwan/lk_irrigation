# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--18_09:16:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **182,568 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 09:16:40 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:10:58 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:10:50 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-06-18 09:10:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:09:44 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 09:08:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:08:07 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.059 |  |
| 2026-06-18 09:08:04 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.039 |  |
| 2026-06-18 09:07:38 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:07:30 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.065 |  |
| 2026-06-18 09:07:27 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.052 |  |
| 2026-06-18 09:07:15 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-18 09:05:35 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:05:18 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-06-18 09:04:36 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.019 |  |
| 2026-06-18 09:04:31 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.030 |  |
| 2026-06-18 09:04:16 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-18 09:04:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:04:13 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-18 09:04:08 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 09:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:03:27 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-06-18 09:03:06 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-06-18 09:02:57 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 09:02:55 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:02:48 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.096 |  |
| 2026-06-18 09:02:31 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:02:22 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-06-18 09:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 09:02:11 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-18 09:02:10 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 09:02:06 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:01:56 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:01:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:00:20 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:00:16 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-06-18 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.041 |  |
| 2026-06-18 09:00:11 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:00:03 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-18 09:04:13 | Thalgahagoda (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-06-18 09:04:08 | Putupaula (Kalu Ganga) | 0.99 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-18 09:04:16 | Dunamale (Aththanagalu Oya) | 1.74 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-06-18 09:07:15 | Magura (Kalu Ganga) | 1.87 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-06-18 09:02:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.11 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-18 09:02:10 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 09:02:57 | Giriulla (Maha Oya) | 1.17 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 09:09:44 | Holombuwa (Kelani Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-18 09:00:11 | Wellawaya (Kirindi Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:00:03 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:10:58 | Moragaswewa (Deduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:03:45 | Nawalapitiya (Mahaweli Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:01:38 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-18 08:02:04 | Horowpothana (Yan Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:10:41 | Galgamuwa (Mee Oya) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:08:42 | Norwood (Kelani Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:02:31 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:04:14 | Padiyathalawa (Maduru Oya) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:02:55 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:07:38 | Badalgama (Maha Oya) | 2.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:01:56 | Thanthirimale (Malwathu Oya) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:16:40 | Thawalama (Gin Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:05:35 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:02:06 | Thanamalwila (Kirindi Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-18 09:02:11 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-06-18 09:00:16 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-06-18 09:10:50 | Pitabeddara (Nilwala Ganga) | 1.31 | 🟢 Normal | -0.019 |  |
| 2026-06-18 09:04:36 | Manampitiya (Mahaweli Ganga) | -0.09 | 🟢 Normal | -0.019 |  |
| 2026-06-18 09:02:22 | Peradeniya (Mahaweli Ganga) | 1.76 | 🟢 Normal | -0.021 |  |
| 2026-06-18 09:03:06 | Deraniyagala (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-06-18 09:04:31 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.030 |  |
| 2026-06-18 09:08:04 | Panadugama (Nilwala Ganga) | 3.76 | 🟢 Normal | -0.039 |  |
| 2026-06-18 09:00:14 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.041 |  |
| 2026-06-18 09:03:27 | Urawa (Nilwala Ganga) | 0.65 | 🟢 Normal | -0.049 |  |
| 2026-06-18 09:07:27 | Rathnapura (Kalu Ganga) | 2.04 | 🟢 Normal | -0.052 |  |
| 2026-06-18 09:08:07 | Glencourse (Kelani Ganga) | 10.56 | 🟢 Normal | -0.059 |  |
| 2026-06-18 09:07:30 | Ellagawa (Kalu Ganga) | 6.12 | 🟢 Normal | -0.065 |  |
| 2026-06-18 09:05:18 | Kithulgala (Kelani Ganga) | 1.64 | 🟢 Normal | -0.068 |  |
| 2026-06-18 09:02:48 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)