# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--05_09:07:50-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **279,439 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 09:07:50 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:07:25 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:07:19 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.079 |  |
| 2026-10-05 09:07:01 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-10-05 09:06:48 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.038 |  |
| 2026-10-05 09:06:26 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-10-05 09:06:25 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-05 09:06:07 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-10-05 09:05:56 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-10-05 09:04:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:04:52 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.036 |  |
| 2026-10-05 09:04:39 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.050 |  |
| 2026-10-05 09:04:34 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-10-05 09:04:33 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:04:24 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-10-05 09:04:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 09:04:08 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.077 |  |
| 2026-10-05 09:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:03:42 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 09:03:34 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:03:24 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-05 09:03:20 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.110 |  |
| 2026-10-05 09:03:20 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.117 |  |
| 2026-10-05 09:03:03 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:03:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:02:46 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-10-05 09:02:41 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.011 |  |
| 2026-10-05 09:02:30 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-05 09:02:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:02:22 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:02:16 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-10-05 09:02:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 09:02:04 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:01:54 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.039 |  |
| 2026-10-05 09:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:01:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:00:48 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.026 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-05 09:02:30 | Horowpothana (Yan Oya) | 1.96 | 🟢 Normal | 0.276 | 🔺 Rising |
| 2026-10-05 09:03:24 | Thalgahagoda (Nilwala Ganga) | 0.75 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-10-05 09:04:11 | Nagalagam Street (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-05 09:00:48 | Thanthirimale (Malwathu Oya) | 0.78 | 🟢 Normal | 0.026 | 🔺 Rising |
| 2026-10-05 09:02:16 | Wellawaya (Kirindi Oya) | 1.05 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-05 09:06:25 | Pitabeddara (Nilwala Ganga) | 0.99 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-05 09:03:42 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-05 09:02:23 | Moragaswewa (Deduru Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:01:22 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:03:01 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:04:54 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:07:50 | Badalgama (Maha Oya) | 3.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:02:22 | Kuda Oya (Kirindi Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-10-05 09:04:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:07:25 | Urawa (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.41 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:04:33 | Siyambalanduwa (Heda Oya) | 0.32 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:03:03 | Ellagawa (Kalu Ganga) | 6.21 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:03:34 | Norwood (Kelani Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:02:04 | Deraniyagala (Kelani Ganga) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-10-05 09:02:41 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | -0.011 |  |
| 2026-10-05 09:04:34 | Thawalama (Gin Ganga) | 1.97 | 🟢 Normal | -0.011 |  |
| 2026-10-05 09:05:56 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | -0.019 |  |
| 2026-10-05 09:04:24 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.019 |  |
| 2026-10-05 09:02:16 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.020 |  |
| 2026-10-05 09:07:01 | Baddegama (Gin Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-10-05 09:06:26 | Holombuwa (Kelani Ganga) | 0.92 | 🟢 Normal | -0.021 |  |
| 2026-10-05 08:10:47 | Panadugama (Nilwala Ganga) | 3.72 | 🟢 Normal | -0.032 |  |
| 2026-10-05 09:04:52 | Rathnapura (Kalu Ganga) | 1.83 | 🟢 Normal | -0.036 |  |
| 2026-10-05 09:06:07 | Thaldena (Mahaweli Ganga) | 0.26 | 🟢 Normal | -0.038 |  |
| 2026-10-05 09:06:48 | Magura (Kalu Ganga) | 1.79 | 🟢 Normal | -0.038 |  |
| 2026-10-05 09:01:54 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | -0.039 |  |
| 2026-10-05 09:04:39 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.050 |  |
| 2026-10-05 08:01:56 | Dunamale (Aththanagalu Oya) | 2.69 | 🟢 Normal | -0.053 |  |
| 2026-10-05 09:02:46 | Giriulla (Maha Oya) | 1.91 | 🟢 Normal | -0.061 |  |
| 2026-10-05 09:04:08 | Peradeniya (Mahaweli Ganga) | 3.22 | 🟢 Normal | -0.077 |  |
| 2026-10-05 09:07:19 | Thanamalwila (Kirindi Oya) | 0.32 | 🟢 Normal | -0.079 |  |
| 2026-10-05 09:03:20 | Hanwella (Kelani Ganga) | 3.74 | 🟢 Normal | -0.110 |  |
| 2026-10-05 09:03:20 | Glencourse (Kelani Ganga) | 11.51 | 🟢 Normal | -0.117 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)