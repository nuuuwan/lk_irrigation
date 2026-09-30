# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_00:10:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **275,484 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **29** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 00:10:28 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-10-01 00:09:25 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:08:59 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:08:00 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:07:34 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:06:55 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-10-01 00:06:27 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -1.995 |  |
| 2026-10-01 00:06:25 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -3.051 |  |
| 2026-10-01 00:06:24 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-01 00:05:39 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-01 00:05:34 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.009 |  |
| 2026-10-01 00:04:45 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:04:43 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-01 00:04:32 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-10-01 00:04:27 | Norwood (Kelani Ganga) | 0.84 | 🟢 Normal | -3.051 |  |
| 2026-10-01 00:04:09 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:04:02 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-10-01 00:03:39 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:03:24 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:03:23 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:02:52 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-10-01 00:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:02:26 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 00:02:25 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 00:01:52 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-10-01 00:01:08 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:00:38 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-01 00:00:12 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:59:14 | Peradeniya (Mahaweli Ganga) | 3.08 | 🟢 Normal | -1.995 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-09-30 18:00:36 | Weraganthota (Mahaweli Ganga) | -3.39 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-10-01 00:06:24 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-10-01 00:04:43 | Hanwella (Kelani Ganga) | 2.04 | 🟢 Normal | 0.038 | 🔺 Rising |
| 2026-10-01 00:00:38 | Nakkala (Kumbukkan Oya) | 0.56 | 🟢 Normal | 0.036 | 🔺 Rising |
| 2026-10-01 00:05:39 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-10-01 00:02:25 | Glencourse (Kelani Ganga) | 10.37 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 00:02:26 | Manampitiya (Mahaweli Ganga) | -0.32 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 00:09:25 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:03:39 | Moragaswewa (Deduru Oya) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:02:43 | Nawalapitiya (Mahaweli Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:10:16 | Yaka Wewa (Ma Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:03:24 | Giriulla (Maha Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-09-30 18:27:28 | Galgamuwa (Mee Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:03:23 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:00:12 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:01:08 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:07:34 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:04:09 | Badalgama (Maha Oya) | 2.16 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:08:00 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:15:48 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-09-30 17:00:54 | Thanthirimale (Malwathu Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:03:38 | Urawa (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-10-01 00:04:45 | Kuda Oya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-09-30 23:09:18 | Magura (Kalu Ganga) | 1.68 | 🟢 Normal | -0.009 |  |
| 2026-10-01 00:05:34 | Panadugama (Nilwala Ganga) | 3.27 | 🟢 Normal | -0.009 |  |
| 2026-10-01 00:02:52 | Siyambalanduwa (Heda Oya) | 0.21 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:01:12 | Horowpothana (Yan Oya) | 1.87 | 🟢 Normal | -0.010 |  |
| 2026-09-30 23:01:34 | Ellagawa (Kalu Ganga) | 5.17 | 🟢 Normal | -0.010 |  |
| 2026-10-01 00:04:32 | Thawalama (Gin Ganga) | 1.84 | 🟢 Normal | -0.010 |  |
| 2026-09-30 22:56:32 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | -0.011 |  |
| 2026-10-01 00:01:52 | Pitabeddara (Nilwala Ganga) | 0.96 | 🟢 Normal | -0.011 |  |
| 2026-10-01 00:10:28 | Thalgahagoda (Nilwala Ganga) | 0.63 | 🟢 Normal | -0.019 |  |
| 2026-10-01 00:06:55 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | -0.019 |  |
| 2026-09-30 23:01:55 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.62 | 🟢 Normal | -0.020 |  |
| 2026-09-30 23:09:54 | Baddegama (Gin Ganga) | 2.00 | 🟢 Normal | -0.028 |  |
| 2026-10-01 00:04:02 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | -0.040 |  |
| 2026-09-30 23:05:48 | Putupaula (Kalu Ganga) | 0.35 | 🟢 Normal | -0.111 |  |
| 2026-10-01 00:06:27 | Peradeniya (Mahaweli Ganga) | 2.84 | 🟢 Normal | -1.995 |  |
| 2026-10-01 00:06:25 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -3.051 |  |

## River Water Level Charts by Station

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)