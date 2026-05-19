# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--19_07:31:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **155,864 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 07:31:06 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-05-19 07:25:19 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:23:40 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-05-19 07:21:31 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.023 |  |
| 2026-05-19 07:15:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-19 07:13:00 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-19 07:09:45 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-19 07:08:57 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:08:17 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-05-19 07:07:54 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-05-19 07:07:48 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:07:37 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.072 |  |
| 2026-05-19 07:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | -0.084 |  |
| 2026-05-19 07:05:53 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:05:29 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:04:28 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:04:21 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 07:03:41 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:03:38 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:03:23 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-05-19 07:03:14 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.040 |  |
| 2026-05-19 07:03:09 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.096 |  |
| 2026-05-19 07:02:48 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.030 |  |
| 2026-05-19 07:02:41 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-19 07:02:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-19 07:02:37 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2026-05-19 07:02:22 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:02:20 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-05-19 07:02:19 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:02:19 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:02:03 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.069 |  |
| 2026-05-19 07:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-19 07:01:46 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.023 |  |
| 2026-05-19 07:01:32 | Thanthirimale (Malwathu Oya) | 2.51 | 🟢 Normal | -0.018 |  |
| 2026-05-19 07:01:31 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-19 07:00:53 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-05-19 07:00:46 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.043 |  |
| 2026-05-19 07:00:45 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:00:41 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-05-19 07:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-19 07:15:32 | Kithulgala (Kelani Ganga) | 1.60 | 🟢 Normal | 0.065 | 🔺 Rising |
| 2026-05-19 07:09:45 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-05-19 07:13:00 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-05-19 07:01:56 | Nawalapitiya (Mahaweli Ganga) | 1.09 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-05-19 07:04:21 | Hanwella (Kelani Ganga) | 2.07 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-19 07:00:45 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:25:19 | Moragaswewa (Deduru Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:02:22 | Yaka Wewa (Ma Oya) | 0.61 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:07:48 | Galgamuwa (Mee Oya) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:02:19 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:03:38 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:02:19 | Deraniyagala (Kelani Ganga) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:05:53 | Ellagawa (Kalu Ganga) | 5.58 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:05:29 | Panadugama (Nilwala Ganga) | 2.62 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:04:28 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:00:12 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:08:57 | Urawa (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-05-19 07:08:17 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.009 |  |
| 2026-05-19 07:02:40 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | -0.010 |  |
| 2026-05-19 07:02:41 | Giriulla (Maha Oya) | 1.65 | 🟢 Normal | -0.010 |  |
| 2026-05-19 07:01:31 | Kuda Oya (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-19 07:00:53 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | -0.011 |  |
| 2026-05-19 07:02:37 | Baddegama (Gin Ganga) | 1.67 | 🟢 Normal | -0.011 |  |
| 2026-05-19 07:31:06 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | -0.013 |  |
| 2026-05-19 07:01:32 | Thanthirimale (Malwathu Oya) | 2.51 | 🟢 Normal | -0.018 |  |
| 2026-05-19 07:03:23 | Badalgama (Maha Oya) | 2.94 | 🟢 Normal | -0.020 |  |
| 2026-05-19 07:21:31 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.023 |  |
| 2026-05-19 07:23:40 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.023 |  |
| 2026-05-19 07:01:46 | Rathnapura (Kalu Ganga) | 1.64 | 🟢 Normal | -0.023 |  |
| 2026-05-19 07:02:48 | Katharagama (Menik Ganga) | 0.01 | 🟢 Normal | -0.030 |  |
| 2026-05-19 07:02:20 | Thanamalwila (Kirindi Oya) | 1.04 | 🟢 Normal | -0.030 |  |
| 2026-05-19 07:00:41 | Manampitiya (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.030 |  |
| 2026-05-19 07:07:54 | Peradeniya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.037 |  |
| 2026-05-19 07:03:14 | Glencourse (Kelani Ganga) | 10.03 | 🟢 Normal | -0.040 |  |
| 2026-05-19 07:00:46 | Dunamale (Aththanagalu Oya) | 1.80 | 🟢 Normal | -0.043 |  |
| 2026-05-19 07:02:03 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | -0.069 |  |
| 2026-05-19 07:07:37 | Putupaula (Kalu Ganga) | 1.20 | 🟢 Normal | -0.072 |  |
| 2026-05-19 07:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.07 | 🟢 Normal | -0.084 |  |
| 2026-05-19 07:03:09 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.096 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)