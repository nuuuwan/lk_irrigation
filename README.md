# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--13_05:15:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **177,961 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 05:15:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-06-13 05:15:12 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | -0.078 |  |
| 2026-06-13 05:13:46 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-13 05:11:52 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-13 05:11:31 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -13.263 |  |
| 2026-06-13 05:11:12 | Urawa (Nilwala Ganga) | 1.32 | 🟢 Normal | -13.263 |  |
| 2026-06-13 05:11:00 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.056 |  |
| 2026-06-13 05:08:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.073 |  |
| 2026-06-13 05:08:19 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:07:34 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-13 05:07:32 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-13 05:06:27 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.087 |  |
| 2026-06-13 05:04:26 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-13 05:04:23 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-13 05:04:15 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-13 05:03:56 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.156 |  |
| 2026-06-13 05:03:45 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:03:38 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 05:03:38 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.155 |  |
| 2026-06-13 05:03:26 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-06-13 05:02:56 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-13 05:02:54 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-13 05:02:46 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-13 05:02:45 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-13 05:02:31 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:02:19 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-13 05:01:56 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:53 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-13 05:01:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:32 | Ellagawa (Kalu Ganga) | 8.47 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-06-13 05:01:16 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 05:01:11 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:09 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:03 | Ellagawa (Kalu Ganga) | 8.42 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-06-13 05:00:58 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:00:52 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-06-13 04:59:40 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.012 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-13 05:15:47 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.30 | 🟡 Alert | 0.028 | 🔺 Rising |
| 2026-06-13 05:11:00 | Magura (Kalu Ganga) | 4.60 | 🟡 Alert | -0.056 |  |
| 2026-06-13 05:15:12 | Rathnapura (Kalu Ganga) | 6.08 | 🟡 Alert | -0.078 |  |
| 2026-06-13 05:02:56 | Nakkala (Kumbukkan Oya) | 0.79 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-06-13 05:01:32 | Ellagawa (Kalu Ganga) | 8.47 | 🟢 Normal | 6.207 | 🔺 Rising |
| 2026-06-13 05:04:26 | Giriulla (Maha Oya) | 2.43 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-06-13 05:13:46 | Holombuwa (Kelani Ganga) | 1.46 | 🟢 Normal | 0.056 | 🔺 Rising |
| 2026-06-13 05:01:53 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-13 05:07:32 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-06-13 05:07:34 | Nawalapitiya (Mahaweli Ganga) | 1.92 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-06-13 05:02:45 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-13 05:02:19 | Dunamale (Aththanagalu Oya) | 3.23 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-12 18:04:11 | Galgamuwa (Mee Oya) | 0.51 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-06-13 05:01:16 | Peradeniya (Mahaweli Ganga) | 2.57 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-13 05:11:52 | Baddegama (Gin Ganga) | 3.13 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-13 05:04:23 | Panadugama (Nilwala Ganga) | 4.87 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-06-13 05:03:38 | Thalgahagoda (Nilwala Ganga) | 1.04 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-13 05:08:19 | Kithulgala (Kelani Ganga) | 1.89 | 🟢 Normal | 0.000 |  |
| 2026-06-12 18:02:22 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:00:58 | Wellawaya (Kirindi Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:56 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:03:45 | Horowpothana (Yan Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:02:31 | Norwood (Kelani Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:11 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:50 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-12 19:19:51 | Thanthirimale (Malwathu Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-06-13 05:01:09 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-06-13 04:04:04 | Katharagama (Menik Ganga) | 0.03 | 🟢 Normal | -0.010 |  |
| 2026-06-13 05:04:15 | Badalgama (Maha Oya) | 3.38 | 🟢 Normal | -0.010 |  |
| 2026-06-13 05:03:26 | Hanwella (Kelani Ganga) | 4.20 | 🟢 Normal | -0.011 |  |
| 2026-06-13 04:59:40 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | -0.012 |  |
| 2026-06-13 04:08:38 | Moraketiya (Walawe Ganga) | 1.40 | 🟢 Normal | -0.018 |  |
| 2026-06-13 05:00:52 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.020 |  |
| 2026-06-13 05:02:46 | Deraniyagala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.020 |  |
| 2026-06-13 05:08:25 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.073 |  |
| 2026-06-13 05:06:27 | Glencourse (Kelani Ganga) | 12.00 | 🟢 Normal | -0.087 |  |
| 2026-06-13 05:03:38 | Thawalama (Gin Ganga) | 3.47 | 🟢 Normal | -0.155 |  |
| 2026-06-13 05:03:56 | Pitabeddara (Nilwala Ganga) | 2.05 | 🟢 Normal | -0.156 |  |
| 2026-06-13 05:11:31 | Urawa (Nilwala Ganga) | 1.25 | 🟢 Normal | -13.263 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)