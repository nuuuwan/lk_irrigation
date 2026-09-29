# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--09--29_08:12:00-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **273,978 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 08:12:00 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:11:45 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | -0.019 |  |
| 2026-09-29 08:11:26 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:10:40 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:07:33 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:06:50 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-09-29 08:06:38 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-29 08:06:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:06:27 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:05:58 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:05:13 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-09-29 08:04:56 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:04:48 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:04:41 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:04:36 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.072 |  |
| 2026-09-29 08:04:35 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:04:00 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.081 |  |
| 2026-09-29 08:03:43 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 08:03:31 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:03:22 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:03:14 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-29 08:03:03 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:02:30 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:02:06 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:02:04 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.152 |  |
| 2026-09-29 08:01:53 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-29 08:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.049 |  |
| 2026-09-29 08:01:08 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.013 |  |
| 2026-09-29 08:00:55 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:00:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:00:29 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.077 |  |
| 2026-09-29 08:00:24 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:00:08 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:00:06 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:41:42 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -6.968 |  |
| 2026-09-29 07:41:11 | Horowpothana (Yan Oya) | 1.97 | 🟢 Normal | -6.968 |  |
| 2026-09-29 07:31:40 | Thalgahagoda (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.043 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-29 08:06:38 | Peradeniya (Mahaweli Ganga) | 2.78 | 🟢 Normal | 0.164 | 🔺 Rising |
| 2026-09-29 08:01:53 | Manampitiya (Mahaweli Ganga) | -0.30 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-09-29 08:03:43 | Ellagawa (Kalu Ganga) | 5.98 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-09-29 08:03:14 | Hanwella (Kelani Ganga) | 2.84 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-09-29 08:00:08 | Wellawaya (Kirindi Oya) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:00:06 | Nakkala (Kumbukkan Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:03:31 | Moragaswewa (Deduru Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:01:40 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:12:00 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:06:30 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:07:33 | Magura (Kalu Ganga) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:06:27 | Pitabeddara (Nilwala Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:10:40 | Norwood (Kelani Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:00:33 | Padiyathalawa (Maduru Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:04:41 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:02:30 | Siyambalanduwa (Heda Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:04:35 | Dunamale (Aththanagalu Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:04:48 | Katharagama (Menik Ganga) | -0.29 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:11:26 | Badalgama (Maha Oya) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:00:55 | Thanthirimale (Malwathu Oya) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:28:05 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-09-29 08:03:03 | Kuda Oya (Kirindi Oya) | 0.89 | 🟢 Normal | 0.000 |  |
| 2026-09-29 07:08:21 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.54 | 🟢 Normal | -0.009 |  |
| 2026-09-29 08:06:50 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.009 |  |
| 2026-09-29 08:03:22 | Deraniyagala (Kelani Ganga) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:02:06 | Thanamalwila (Kirindi Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:05:58 | Moraketiya (Walawe Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:04:56 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | -0.010 |  |
| 2026-09-29 08:01:08 | Panadugama (Nilwala Ganga) | 3.69 | 🟢 Normal | -0.013 |  |
| 2026-09-29 08:11:45 | Baddegama (Gin Ganga) | 3.26 | 🟢 Normal | -0.019 |  |
| 2026-09-29 08:05:13 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.020 |  |
| 2026-09-29 07:04:02 | Thaldena (Mahaweli Ganga) | 0.02 | 🟢 Normal | -0.021 |  |
| 2026-09-29 07:31:40 | Thalgahagoda (Nilwala Ganga) | 1.32 | 🟢 Normal | -0.043 |  |
| 2026-09-29 08:01:25 | Nawalapitiya (Mahaweli Ganga) | 1.71 | 🟢 Normal | -0.049 |  |
| 2026-09-29 08:04:36 | Rathnapura (Kalu Ganga) | 2.36 | 🟢 Normal | -0.072 |  |
| 2026-09-29 08:00:29 | Weraganthota (Mahaweli Ganga) | -3.12 | 🟢 Normal | -0.077 |  |
| 2026-09-29 08:04:00 | Putupaula (Kalu Ganga) | 1.02 | 🟢 Normal | -0.081 |  |
| 2026-09-29 08:02:04 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | -0.152 |  |
| 2026-09-29 07:41:42 | Horowpothana (Yan Oya) | 1.91 | 🟢 Normal | -6.968 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)