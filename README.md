# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--06_00:25:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **226,016 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Peradeniya — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 00:25:30 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:23:59 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.081 |  |
| 2026-08-06 00:18:55 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:18:53 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:18:40 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-08-06 00:14:42 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.017 |  |
| 2026-08-06 00:09:37 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:09:16 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:09:07 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.113 |  |
| 2026-08-06 00:08:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:08:34 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:07:06 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:06:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:06:32 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.078 |  |
| 2026-08-06 00:06:01 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:05:24 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.031 |  |
| 2026-08-06 00:05:22 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:04:54 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:04:48 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:04:02 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:03:53 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.088 |  |
| 2026-08-06 00:03:52 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:03:16 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:03:09 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-08-06 00:03:07 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:03:02 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.67 | 🟢 Normal | -0.021 |  |
| 2026-08-06 00:02:41 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:02:34 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:02:19 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.050 |  |
| 2026-08-06 00:02:18 | Peradeniya (Mahaweli Ganga) | 5.00 | 🟡 Alert | -0.403 |  |
| 2026-08-06 00:01:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-08-06 00:01:37 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:01:34 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:01:30 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 00:01:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:01:14 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:01:10 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:00:24 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-06 00:02:18 | Peradeniya (Mahaweli Ganga) | 5.00 | 🟡 Alert | -0.403 |  |
| 2026-08-06 00:01:30 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-06 00:06:01 | Wellawaya (Kirindi Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:08:58 | Nakkala (Kumbukkan Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:02:41 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:06:54 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:03:07 | Giriulla (Maha Oya) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:11:01 | Galgamuwa (Mee Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:25:30 | Magura (Kalu Ganga) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:09:16 | Pitabeddara (Nilwala Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:01:17 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:00:24 | Moraketiya (Walawe Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:03:02 | Siyambalanduwa (Heda Oya) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:08:34 | Thaldena (Mahaweli Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:04:02 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:05:22 | Putupaula (Kalu Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:03:52 | Badalgama (Maha Oya) | 2.36 | 🟢 Normal | 0.000 |  |
| 2026-08-05 18:09:25 | Thanthirimale (Malwathu Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:18:55 | Thawalama (Gin Ganga) | 1.59 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:09:37 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:01:10 | Kuda Oya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:07:06 | Thanamalwila (Kirindi Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-06 00:18:40 | Norwood (Kelani Ganga) | 0.97 | 🟢 Normal | -0.009 |  |
| 2026-08-05 18:01:36 | Weraganthota (Mahaweli Ganga) | -3.49 | 🟢 Normal | -0.010 |  |
| 2026-08-06 00:14:42 | Holombuwa (Kelani Ganga) | 0.68 | 🟢 Normal | -0.017 |  |
| 2026-08-06 00:03:09 | Panadugama (Nilwala Ganga) | 2.61 | 🟢 Normal | -0.019 |  |
| 2026-08-06 00:01:34 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:03:16 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:01:37 | Nawalapitiya (Mahaweli Ganga) | 2.22 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:04:48 | Deraniyagala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:01:14 | Kithulgala (Kelani Ganga) | 2.50 | 🟢 Normal | -0.020 |  |
| 2026-08-06 00:02:48 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.67 | 🟢 Normal | -0.021 |  |
| 2026-08-06 00:05:24 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.031 |  |
| 2026-08-06 00:02:19 | Baddegama (Gin Ganga) | 1.37 | 🟢 Normal | -0.050 |  |
| 2026-08-06 00:01:42 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | -0.061 |  |
| 2026-08-06 00:06:32 | Glencourse (Kelani Ganga) | 11.65 | 🟢 Normal | -0.078 |  |
| 2026-08-06 00:23:59 | Ellagawa (Kalu Ganga) | 8.50 | 🟢 Normal | -0.081 |  |
| 2026-08-06 00:03:53 | Hanwella (Kelani Ganga) | 3.73 | 🟢 Normal | -0.088 |  |
| 2026-08-06 00:09:07 | Rathnapura (Kalu Ganga) | 3.29 | 🟢 Normal | -0.113 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)