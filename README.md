# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_04:35:03-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,625 measurements** from **39** stations.
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
| 2026-10-11 04:35:03 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:32:03 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-11 04:25:02 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-11 04:16:17 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-11 04:11:33 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.057 |  |
| 2026-10-11 04:11:25 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-10-11 04:08:34 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | -0.134 |  |
| 2026-10-11 04:06:31 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-11 04:06:10 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 04:06:09 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.073 |  |
| 2026-10-11 04:05:52 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 04:05:46 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.020 |  |
| 2026-10-11 04:05:07 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-11 04:05:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:04:52 | Giriulla (Maha Oya) | 3.26 | 🟢 Normal | -0.068 |  |
| 2026-10-11 04:04:45 | Badalgama (Maha Oya) | 4.04 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-11 04:04:15 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-11 04:04:12 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.025 |  |
| 2026-10-11 04:04:00 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 04:03:35 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.040 |  |
| 2026-10-11 04:02:49 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2026-10-11 04:02:45 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-11 04:02:41 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:02:32 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.022 |  |
| 2026-10-11 04:02:27 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.070 |  |
| 2026-10-11 04:02:21 | Moragaswewa (Deduru Oya) | 2.00 | 🟢 Normal | -0.251 |  |
| 2026-10-11 04:02:04 | Peradeniya (Mahaweli Ganga) | 3.29 | 🟢 Normal | -0.062 |  |
| 2026-10-11 04:01:56 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.032 |  |
| 2026-10-11 04:01:46 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 04:01:23 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 04:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-11 04:01:13 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 04:01:07 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 04:04:45 | Badalgama (Maha Oya) | 4.04 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-10-11 04:02:45 | Magura (Kalu Ganga) | 3.86 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-10-11 04:04:15 | Hanwella (Kelani Ganga) | 3.07 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-10-11 04:04:00 | Kithulgala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-11 03:02:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.16 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-11 04:05:52 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-11 04:01:13 | Kuda Oya (Kirindi Oya) | 1.67 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-11 04:05:07 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-11 04:16:17 | Baddegama (Gin Ganga) | 2.01 | 🟢 Normal | 0.025 | 🔺 Rising |
| 2026-10-11 04:25:02 | Thalgahagoda (Nilwala Ganga) | 0.97 | 🟢 Normal | 0.024 | 🔺 Rising |
| 2026-10-11 04:32:03 | Putupaula (Kalu Ganga) | 1.13 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-10-11 04:06:10 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 04:01:23 | Ellagawa (Kalu Ganga) | 6.51 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 04:01:46 | Glencourse (Kelani Ganga) | 11.21 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 01:01:45 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:05:05 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:01:26 | Galgamuwa (Mee Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:02:41 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:35:03 | Moraketiya (Walawe Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-10-11 03:09:30 | Holombuwa (Kelani Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-10-10 18:00:50 | Thanthirimale (Malwathu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 04:01:13 | Nawalapitiya (Mahaweli Ganga) | 1.23 | 🟢 Normal | -0.010 |  |
| 2026-10-11 04:05:46 | Panadugama (Nilwala Ganga) | 4.02 | 🟢 Normal | -0.020 |  |
| 2026-10-11 04:01:07 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | -0.020 |  |
| 2026-10-11 04:02:32 | Thanamalwila (Kirindi Oya) | 0.88 | 🟢 Normal | -0.022 |  |
| 2026-10-11 04:04:12 | Siyambalanduwa (Heda Oya) | 0.40 | 🟢 Normal | -0.025 |  |
| 2026-10-11 04:06:31 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.030 |  |
| 2026-10-11 04:01:56 | Manampitiya (Mahaweli Ganga) | -0.04 | 🟢 Normal | -0.032 |  |
| 2026-10-11 04:03:35 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.040 |  |
| 2026-10-11 04:02:49 | Norwood (Kelani Ganga) | 1.01 | 🟢 Normal | -0.043 |  |
| 2026-10-10 18:05:26 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.050 |  |
| 2026-10-11 04:11:33 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.057 |  |
| 2026-10-11 04:02:04 | Peradeniya (Mahaweli Ganga) | 3.29 | 🟢 Normal | -0.062 |  |
| 2026-10-11 04:04:52 | Giriulla (Maha Oya) | 3.26 | 🟢 Normal | -0.068 |  |
| 2026-10-11 04:02:27 | Nakkala (Kumbukkan Oya) | 1.25 | 🟢 Normal | -0.070 |  |
| 2026-10-11 04:06:09 | Thaldena (Mahaweli Ganga) | 0.89 | 🟢 Normal | -0.073 |  |
| 2026-10-11 04:11:25 | Deraniyagala (Kelani Ganga) | 0.90 | 🟢 Normal | -0.082 |  |
| 2026-10-11 04:08:34 | Thawalama (Gin Ganga) | 3.19 | 🟢 Normal | -0.134 |  |
| 2026-10-11 04:02:21 | Moragaswewa (Deduru Oya) | 2.00 | 🟢 Normal | -0.251 |  |

## River Water Level Charts by Station

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

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

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)