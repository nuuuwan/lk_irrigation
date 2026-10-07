# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--07_19:08:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **281,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **33** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 19:08:28 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:08:18 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-07 19:08:01 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.029 |  |
| 2026-10-07 19:07:42 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-10-07 19:07:16 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-07 19:07:14 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-07 19:05:53 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-10-07 19:05:50 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-07 19:05:31 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.038 |  |
| 2026-10-07 19:05:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:05:17 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-10-07 19:05:06 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:05:02 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-07 19:04:52 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.046 |  |
| 2026-10-07 19:04:32 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 19:04:31 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.049 |  |
| 2026-10-07 19:04:22 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-07 19:04:09 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-10-07 19:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.032 |  |
| 2026-10-07 19:04:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:04:02 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-07 19:03:50 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-10-07 19:03:30 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:03:17 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.010 |  |
| 2026-10-07 19:03:07 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:03:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:02:55 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-07 19:02:37 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-07 19:02:10 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.070 |  |
| 2026-10-07 19:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:01:32 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.030 |  |
| 2026-10-07 19:01:08 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-07 19:00:41 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-07 19:07:42 | Peradeniya (Mahaweli Ganga) | 2.49 | 🟢 Normal | 0.393 | 🔺 Rising |
| 2026-10-07 19:05:50 | Thawalama (Gin Ganga) | 2.53 | 🟢 Normal | 0.155 | 🔺 Rising |
| 2026-10-07 19:08:18 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-07 19:07:16 | Rathnapura (Kalu Ganga) | 1.82 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-10-07 19:07:14 | Glencourse (Kelani Ganga) | 10.60 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-10-07 19:05:02 | Magura (Kalu Ganga) | 2.15 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-10-07 19:02:37 | Kithulgala (Kelani Ganga) | 1.92 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-07 19:04:32 | Nawalapitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-07 18:02:42 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-07 18:03:09 | Weraganthota (Mahaweli Ganga) | -3.45 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-07 19:00:41 | Wellawaya (Kirindi Oya) | 0.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-07 19:02:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:03:30 | Horowpothana (Yan Oya) | 1.65 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:03:15 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:05:06 | Padiyathalawa (Maduru Oya) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:04:03 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:05:30 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:03:07 | Siyambalanduwa (Heda Oya) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:08:28 | Katharagama (Menik Ganga) | -0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-07 18:09:53 | Thanthirimale (Malwathu Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:03:04 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-07 19:02:55 | Norwood (Kelani Ganga) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-10-07 19:01:08 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-10-07 19:04:22 | Thanamalwila (Kirindi Oya) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-10-07 19:03:17 | Ellagawa (Kalu Ganga) | 5.47 | 🟢 Normal | -0.010 |  |
| 2026-10-07 18:10:07 | Urawa (Nilwala Ganga) | 0.42 | 🟢 Normal | -0.011 |  |
| 2026-10-07 19:04:09 | Thalgahagoda (Nilwala Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-10-07 19:03:50 | Giriulla (Maha Oya) | 1.53 | 🟢 Normal | -0.020 |  |
| 2026-10-07 19:04:02 | Dunamale (Aththanagalu Oya) | 1.88 | 🟢 Normal | -0.020 |  |
| 2026-10-07 19:05:17 | Baddegama (Gin Ganga) | 2.40 | 🟢 Normal | -0.021 |  |
| 2026-10-07 19:08:01 | Badalgama (Maha Oya) | 2.86 | 🟢 Normal | -0.029 |  |
| 2026-10-07 19:05:53 | Pitabeddara (Nilwala Ganga) | 1.25 | 🟢 Normal | -0.029 |  |
| 2026-10-07 19:01:32 | Manampitiya (Mahaweli Ganga) | -0.08 | 🟢 Normal | -0.030 |  |
| 2026-10-07 19:04:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.32 | 🟢 Normal | -0.032 |  |
| 2026-10-07 18:12:09 | Panadugama (Nilwala Ganga) | 4.85 | 🟢 Normal | -0.036 |  |
| 2026-10-07 19:05:31 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.038 |  |
| 2026-10-07 19:04:52 | Putupaula (Kalu Ganga) | 0.81 | 🟢 Normal | -0.046 |  |
| 2026-10-07 19:04:31 | Hanwella (Kelani Ganga) | 2.48 | 🟢 Normal | -0.049 |  |
| 2026-10-07 19:02:10 | Thaldena (Mahaweli Ganga) | 0.20 | 🟢 Normal | -0.070 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)