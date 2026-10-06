# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--06_14:16:40-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **280,528 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 14:16:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-06 14:13:11 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:11:44 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.035 |  |
| 2026-10-06 14:08:32 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.090 |  |
| 2026-10-06 14:07:49 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:07:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:06:52 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.045 |  |
| 2026-10-06 14:06:26 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:05:31 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.039 |  |
| 2026-10-06 14:05:28 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:04:29 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:04:29 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.099 |  |
| 2026-10-06 14:04:27 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.068 |  |
| 2026-10-06 14:04:19 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-06 14:03:50 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:03:39 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:03:34 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-06 14:03:30 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-06 14:03:11 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:02:53 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:02:47 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:02:43 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.042 |  |
| 2026-10-06 14:02:38 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:02:29 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.039 |  |
| 2026-10-06 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.071 |  |
| 2026-10-06 14:02:19 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-06 14:02:13 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-10-06 14:02:09 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 14:02:07 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.081 |  |
| 2026-10-06 14:02:05 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:01:17 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-06 14:01:04 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 14:01:03 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:00:51 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:24 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.142 |  |
| 2026-10-06 14:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:09 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-06 14:03:34 | Norwood (Kelani Ganga) | 0.96 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-10-06 14:01:17 | Thanamalwila (Kirindi Oya) | 0.67 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-06 14:16:40 | Thalgahagoda (Nilwala Ganga) | 0.70 | 🟢 Normal | 0.017 | 🔺 Rising |
| 2026-10-06 14:01:04 | Thanthirimale (Malwathu Oya) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 14:02:09 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-06 14:00:09 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:03:11 | Moragaswewa (Deduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:23 | Nawalapitiya (Mahaweli Ganga) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:02:05 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:25 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:07:49 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:37 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:02:38 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:00:51 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:04:29 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:03:50 | Holombuwa (Kelani Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:13:11 | Thawalama (Gin Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:07:26 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:05:28 | Kuda Oya (Kirindi Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-10-06 14:02:47 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:02:53 | Wellawaya (Kirindi Oya) | 0.92 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:06:26 | Deraniyagala (Kelani Ganga) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:01:03 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:03:39 | Putupaula (Kalu Ganga) | 1.03 | 🟢 Normal | -0.010 |  |
| 2026-10-06 14:04:19 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-06 14:02:19 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | -0.020 |  |
| 2026-10-06 14:03:30 | Peradeniya (Mahaweli Ganga) | 2.06 | 🟢 Normal | -0.020 |  |
| 2026-10-06 14:02:13 | Giriulla (Maha Oya) | 1.57 | 🟢 Normal | -0.030 |  |
| 2026-10-06 14:11:44 | Dunamale (Aththanagalu Oya) | 2.32 | 🟢 Normal | -0.035 |  |
| 2026-10-06 14:02:29 | Panadugama (Nilwala Ganga) | 3.64 | 🟢 Normal | -0.039 |  |
| 2026-10-06 14:05:31 | Badalgama (Maha Oya) | 2.91 | 🟢 Normal | -0.039 |  |
| 2026-10-06 14:02:43 | Rathnapura (Kalu Ganga) | 1.42 | 🟢 Normal | -0.042 |  |
| 2026-10-06 14:06:52 | Nagalagam Street (Kelani Ganga) | 0.69 | 🟢 Normal | -0.045 |  |
| 2026-10-06 14:04:27 | Glencourse (Kelani Ganga) | 11.25 | 🟢 Normal | -0.068 |  |
| 2026-10-06 14:02:22 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.071 |  |
| 2026-10-06 14:02:07 | Ellagawa (Kalu Ganga) | 5.86 | 🟢 Normal | -0.081 |  |
| 2026-10-06 14:08:32 | Magura (Kalu Ganga) | 1.90 | 🟢 Normal | -0.090 |  |
| 2026-10-06 14:04:29 | Hanwella (Kelani Ganga) | 3.48 | 🟢 Normal | -0.099 |  |
| 2026-10-06 14:00:24 | Weraganthota (Mahaweli Ganga) | -2.79 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)