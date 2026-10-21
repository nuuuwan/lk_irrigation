# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--21_09:09:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **293,855 measurements** from **39** stations.
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
| 2026-10-21 09:09:22 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-10-21 09:08:49 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.029 |  |
| 2026-10-21 09:07:40 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-10-21 09:07:24 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:07:16 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.018 |  |
| 2026-10-21 09:06:57 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:06:32 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:06:23 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:05:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:05:46 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:05:40 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:05:30 | Thalgahagoda (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:04:46 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.022 |  |
| 2026-10-21 09:03:50 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.025 |  |
| 2026-10-21 09:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:03:34 | Moragaswewa (Deduru Oya) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 09:03:32 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-10-21 09:03:15 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:03:13 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-10-21 09:03:09 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:03:05 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 09:03:01 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-10-21 09:02:58 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 09:02:55 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 09:02:53 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:49 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:33 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:32 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:31 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:27 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-10-21 09:02:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:01:49 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.034 |  |
| 2026-10-21 09:01:29 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:01:15 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:01:09 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.236 |  |
| 2026-10-21 09:00:41 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:00:23 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.031 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-21 08:17:45 | Horowpothana (Yan Oya) | 2.16 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-10-21 09:02:58 | Thanthirimale (Malwathu Oya) | 1.78 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-10-21 09:03:05 | Putupaula (Kalu Ganga) | 0.79 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-21 09:03:34 | Moragaswewa (Deduru Oya) | 1.19 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-21 09:02:55 | Manampitiya (Mahaweli Ganga) | 0.53 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-21 09:01:29 | Wellawaya (Kirindi Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:01:15 | Yaka Wewa (Ma Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:49 | Giriulla (Maha Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:32 | Magura (Kalu Ganga) | 1.64 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:06:57 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:03:09 | Hanwella (Kelani Ganga) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:05:58 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:06:23 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:07:24 | Dunamale (Aththanagalu Oya) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:33 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:05:46 | Badalgama (Maha Oya) | 2.53 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:02:53 | Urawa (Nilwala Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:05:30 | Thalgahagoda (Nilwala Ganga) | 1.32 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:00:41 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:03:15 | Thanamalwila (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:03:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.06 | 🟢 Normal | 0.000 |  |
| 2026-10-21 09:07:40 | Pitabeddara (Nilwala Ganga) | 1.30 | 🟢 Normal | -0.009 |  |
| 2026-10-21 09:09:22 | Rathnapura (Kalu Ganga) | 1.93 | 🟢 Normal | -0.009 |  |
| 2026-10-21 09:05:40 | Ellagawa (Kalu Ganga) | 5.59 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:06:32 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:02:23 | Deraniyagala (Kelani Ganga) | 0.87 | 🟢 Normal | -0.010 |  |
| 2026-10-21 09:07:16 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | -0.018 |  |
| 2026-10-21 09:02:27 | Nakkala (Kumbukkan Oya) | 0.97 | 🟢 Normal | -0.019 |  |
| 2026-10-21 09:03:32 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.020 |  |
| 2026-10-21 09:03:13 | Thawalama (Gin Ganga) | 1.88 | 🟢 Normal | -0.021 |  |
| 2026-10-21 08:06:33 | Galgamuwa (Mee Oya) | 1.57 | 🟢 Normal | -0.021 |  |
| 2026-10-21 09:04:46 | Glencourse (Kelani Ganga) | 10.68 | 🟢 Normal | -0.022 |  |
| 2026-10-21 09:03:50 | Padiyathalawa (Maduru Oya) | 0.36 | 🟢 Normal | -0.025 |  |
| 2026-10-21 09:08:49 | Panadugama (Nilwala Ganga) | 4.05 | 🟢 Normal | -0.029 |  |
| 2026-10-21 09:03:01 | Kithulgala (Kelani Ganga) | 2.06 | 🟢 Normal | -0.030 |  |
| 2026-10-21 09:00:23 | Siyambalanduwa (Heda Oya) | 0.75 | 🟢 Normal | -0.031 |  |
| 2026-10-21 09:01:49 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | -0.034 |  |
| 2026-10-21 09:01:09 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | -0.236 |  |

## River Water Level Charts by Station

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)