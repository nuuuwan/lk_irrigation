# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--11_08:23:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **284,780 measurements** from **39** stations.
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
| 2026-10-11 08:23:51 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:22:30 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-10-11 08:17:56 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:10:40 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.017 |  |
| 2026-10-11 08:09:42 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 08:09:18 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 08:08:41 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:07:42 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:07:07 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 08:05:47 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 08:05:41 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.032 |  |
| 2026-10-11 08:05:38 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:05:31 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-10-11 08:05:22 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:04:34 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.047 |  |
| 2026-10-11 08:04:30 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.044 |  |
| 2026-10-11 08:04:00 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-11 08:03:57 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:03:44 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.148 |  |
| 2026-10-11 08:03:42 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.088 |  |
| 2026-10-11 08:03:38 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.030 |  |
| 2026-10-11 08:03:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:03:23 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:02:57 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-11 08:02:45 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-11 08:02:41 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 08:02:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:02:38 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.048 |  |
| 2026-10-11 08:02:18 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.102 |  |
| 2026-10-11 08:02:17 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.052 |  |
| 2026-10-11 08:01:50 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-11 08:01:40 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-10-11 08:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:01:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:01:18 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-10-11 08:00:35 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.140 |  |
| 2026-10-11 08:00:20 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.030 |  |
| 2026-10-11 07:48:58 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-11 08:02:57 | Moragaswewa (Deduru Oya) | 2.35 | 🟢 Normal | 0.098 | 🔺 Rising |
| 2026-10-11 08:09:18 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 08:05:47 | Putupaula (Kalu Ganga) | 1.27 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 07:00:53 | Thanthirimale (Malwathu Oya) | 0.95 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-11 08:06:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.45 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-10-11 08:02:41 | Ellagawa (Kalu Ganga) | 6.60 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 08:09:42 | Baddegama (Gin Ganga) | 2.33 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-11 08:01:33 | Kithulgala (Kelani Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:01:33 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:02:40 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:07:42 | Horowpothana (Yan Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:05:22 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:03:57 | Deraniyagala (Kelani Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:03:23 | Panadugama (Nilwala Ganga) | 4.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:03:37 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:05:38 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:08:41 | Peradeniya (Mahaweli Ganga) | 2.90 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:17:56 | Urawa (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-10-11 08:23:51 | Thalgahagoda (Nilwala Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-10-11 07:48:58 | Pitabeddara (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.006 |  |
| 2026-10-11 08:01:50 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | -0.010 |  |
| 2026-10-11 08:02:45 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-10-11 08:01:40 | Kuda Oya (Kirindi Oya) | 1.57 | 🟢 Normal | -0.011 |  |
| 2026-10-11 08:04:00 | Holombuwa (Kelani Ganga) | 0.93 | 🟢 Normal | -0.011 |  |
| 2026-10-11 08:10:40 | Thanamalwila (Kirindi Oya) | 1.57 | 🟢 Normal | -0.017 |  |
| 2026-10-11 08:01:18 | Dunamale (Aththanagalu Oya) | 3.03 | 🟢 Normal | -0.021 |  |
| 2026-10-11 08:22:30 | Rathnapura (Kalu Ganga) | 2.39 | 🟢 Normal | -0.022 |  |
| 2026-10-11 08:05:31 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | -0.030 |  |
| 2026-10-11 08:03:38 | Hanwella (Kelani Ganga) | 3.04 | 🟢 Normal | -0.030 |  |
| 2026-10-11 08:00:20 | Wellawaya (Kirindi Oya) | 1.28 | 🟢 Normal | -0.030 |  |
| 2026-10-11 08:05:41 | Glencourse (Kelani Ganga) | 11.02 | 🟢 Normal | -0.032 |  |
| 2026-10-11 08:04:30 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.044 |  |
| 2026-10-11 08:04:34 | Nagalagam Street (Kelani Ganga) | 0.35 | 🟢 Normal | -0.047 |  |
| 2026-10-11 08:02:38 | Nakkala (Kumbukkan Oya) | 1.05 | 🟢 Normal | -0.048 |  |
| 2026-10-11 08:02:17 | Badalgama (Maha Oya) | 4.00 | 🟢 Normal | -0.052 |  |
| 2026-10-11 08:03:42 | Magura (Kalu Ganga) | 3.50 | 🟢 Normal | -0.088 |  |
| 2026-10-11 08:02:18 | Giriulla (Maha Oya) | 2.80 | 🟢 Normal | -0.102 |  |
| 2026-10-11 08:00:35 | Weraganthota (Mahaweli Ganga) | -2.96 | 🟢 Normal | -0.140 |  |
| 2026-10-11 08:03:44 | Thawalama (Gin Ganga) | 2.41 | 🟢 Normal | -0.148 |  |

## River Water Level Charts by Station

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)