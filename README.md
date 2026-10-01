# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--01_14:15:22-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **276,027 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 14:15:22 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:12:01 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:11:25 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.026 |  |
| 2026-10-01 14:10:37 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-10-01 14:09:45 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:09:01 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-01 14:07:58 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:07:33 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:07:23 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.091 |  |
| 2026-10-01 14:06:39 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-01 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-01 14:05:49 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:05:48 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.022 |  |
| 2026-10-01 14:05:11 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:05:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-10-01 14:05:00 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:04:42 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:04:31 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:57 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:39 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:36 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.071 |  |
| 2026-10-01 14:03:34 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-01 14:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | -0.059 |  |
| 2026-10-01 14:03:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:03:14 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:08 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:02:53 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:02:38 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | -0.020 |  |
| 2026-10-01 14:02:36 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.029 |  |
| 2026-10-01 14:02:01 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-10-01 14:01:55 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 14:01:47 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:01:42 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:01:40 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:01:35 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-01 14:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:01:25 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-01 14:00:59 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:00:36 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 13:58:27 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-01 14:03:34 | Putupaula (Kalu Ganga) | 0.53 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-10-01 14:05:52 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-10-01 14:01:35 | Thaldena (Mahaweli Ganga) | 0.12 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-10-01 14:09:01 | Panadugama (Nilwala Ganga) | 3.16 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-10-01 14:01:55 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-10-01 14:06:39 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-10-01 14:01:40 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:05:00 | Moragaswewa (Deduru Oya) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:01:26 | Nawalapitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:00 | Yaka Wewa (Ma Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:00:36 | Horowpothana (Yan Oya) | 1.71 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:12:01 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:14 | Hanwella (Kelani Ganga) | 2.02 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:04:31 | Baddegama (Gin Ganga) | 1.69 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:07:58 | Moraketiya (Walawe Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:01:42 | Siyambalanduwa (Heda Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:57 | Katharagama (Menik Ganga) | -0.27 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:05:49 | Holombuwa (Kelani Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:09:45 | Urawa (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:03:08 | Kuda Oya (Kirindi Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-01 14:02:01 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.005 |  |
| 2026-10-01 14:05:08 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | -0.009 |  |
| 2026-10-01 14:07:33 | Thawalama (Gin Ganga) | 1.76 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:05:11 | Ellagawa (Kalu Ganga) | 5.05 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:02:53 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:00:59 | Thanthirimale (Malwathu Oya) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:15:22 | Dunamale (Aththanagalu Oya) | 1.02 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:01:47 | Manampitiya (Mahaweli Ganga) | -0.28 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:03:16 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:04:42 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.010 |  |
| 2026-10-01 14:01:25 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | -0.011 |  |
| 2026-10-01 14:10:37 | Magura (Kalu Ganga) | 1.60 | 🟢 Normal | -0.012 |  |
| 2026-10-01 14:02:38 | Weraganthota (Mahaweli Ganga) | -3.52 | 🟢 Normal | -0.020 |  |
| 2026-10-01 14:05:48 | Glencourse (Kelani Ganga) | 10.34 | 🟢 Normal | -0.022 |  |
| 2026-10-01 14:11:25 | Rathnapura (Kalu Ganga) | 1.40 | 🟢 Normal | -0.026 |  |
| 2026-10-01 14:02:36 | Kithulgala (Kelani Ganga) | 1.94 | 🟢 Normal | -0.029 |  |
| 2026-10-01 14:03:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.57 | 🟢 Normal | -0.059 |  |
| 2026-10-01 14:03:36 | Deraniyagala (Kelani Ganga) | 0.50 | 🟢 Normal | -0.071 |  |
| 2026-10-01 14:07:23 | Peradeniya (Mahaweli Ganga) | 1.88 | 🟢 Normal | -0.091 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)