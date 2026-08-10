# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--10_22:15:18-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **230,020 measurements** from **39** stations.
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
| 2026-08-10 22:15:18 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:11:00 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 22:10:31 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.077 |  |
| 2026-08-10 22:10:31 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:07:48 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 22:06:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.091 |  |
| 2026-08-10 22:05:58 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-10 22:05:33 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:05:29 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:05:04 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-08-10 22:04:57 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-08-10 22:04:25 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-08-10 22:04:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:04:06 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.046 |  |
| 2026-08-10 22:04:00 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-10 22:03:51 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-10 22:03:44 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:39 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 22:03:39 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:11 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:08 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-08-10 22:02:58 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-10 22:02:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-10 22:02:43 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-08-10 22:02:38 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-10 22:02:14 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.066 |  |
| 2026-08-10 22:02:06 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:02:02 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.024 |  |
| 2026-08-10 22:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:01:15 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.060 |  |
| 2026-08-10 22:01:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:01:08 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:00:53 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:00:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:00:38 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-10 22:02:58 | Pitabeddara (Nilwala Ganga) | 0.98 | 🟢 Normal | 18.000 | 🔺 Rising |
| 2026-08-10 22:02:45 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-08-10 22:03:39 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-08-10 22:04:00 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-10 22:07:48 | Glencourse (Kelani Ganga) | 10.36 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-08-10 22:02:02 | Manampitiya (Mahaweli Ganga) | -0.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 22:11:00 | Thawalama (Gin Ganga) | 1.81 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-10 22:00:48 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:36 | Nawalapitiya (Mahaweli Ganga) | 1.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:01:36 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:44 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:00:38 | Horowpothana (Yan Oya) | 1.68 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:02:17 | Galgamuwa (Mee Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:15:18 | Magura (Kalu Ganga) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:11 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:02:06 | Baddegama (Gin Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:01:09 | Padiyathalawa (Maduru Oya) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:01:08 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:00:53 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:04:18 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:05:29 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:03:39 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-10 17:42:25 | Thanthirimale (Malwathu Oya) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:05:33 | Peradeniya (Mahaweli Ganga) | 3.54 | 🟢 Normal | 0.000 |  |
| 2026-08-10 21:06:55 | Kuda Oya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-08-10 22:04:57 | Dunamale (Aththanagalu Oya) | 0.68 | 🟢 Normal | -0.009 |  |
| 2026-08-10 22:05:58 | Wellawaya (Kirindi Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-08-10 22:03:51 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | -0.010 |  |
| 2026-08-10 22:02:43 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.010 |  |
| 2026-08-10 22:04:25 | Urawa (Nilwala Ganga) | 0.26 | 🟢 Normal | -0.012 |  |
| 2026-08-10 22:05:04 | Rathnapura (Kalu Ganga) | 2.14 | 🟢 Normal | -0.020 |  |
| 2026-08-10 22:03:08 | Deraniyagala (Kelani Ganga) | 0.99 | 🟢 Normal | -0.020 |  |
| 2026-08-10 18:00:16 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | -0.020 |  |
| 2026-08-10 22:02:00 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.10 | 🟢 Normal | -0.024 |  |
| 2026-08-10 22:04:06 | Panadugama (Nilwala Ganga) | 3.52 | 🟢 Normal | -0.046 |  |
| 2026-08-10 22:01:15 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | -0.060 |  |
| 2026-08-10 22:02:14 | Hanwella (Kelani Ganga) | 1.88 | 🟢 Normal | -0.066 |  |
| 2026-08-10 22:10:31 | Thalgahagoda (Nilwala Ganga) | 0.86 | 🟢 Normal | -0.077 |  |
| 2026-08-10 22:06:28 | Putupaula (Kalu Ganga) | 0.67 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)