# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--20_00:29:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **238,134 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **21** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 00:29:13 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:15:32 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 00:12:42 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-08-20 00:12:34 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:11:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:09:23 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-08-20 00:09:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.047 |  |
| 2026-08-20 00:08:23 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:07:26 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:07:23 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.048 |  |
| 2026-08-20 00:06:48 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-08-20 00:06:36 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.066 |  |
| 2026-08-20 00:06:06 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-20 00:05:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:05:08 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 00:05:04 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:04:55 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:04:52 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:04:51 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:04:02 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:03:52 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-20 00:03:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-08-20 00:06:06 | Glencourse (Kelani Ganga) | 9.68 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-08-20 00:02:12 | Rathnapura (Kalu Ganga) | 1.50 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-08-20 00:15:32 | Panadugama (Nilwala Ganga) | 2.29 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-20 00:01:39 | Deraniyagala (Kelani Ganga) | 0.86 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 00:05:08 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 00:02:25 | Manampitiya (Mahaweli Ganga) | -0.24 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 00:03:52 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-20 00:08:23 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:04:52 | Nakkala (Kumbukkan Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:04:55 | Moragaswewa (Deduru Oya) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:01:23 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:07:26 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:12:34 | Horowpothana (Yan Oya) | 1.67 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:52 | Galgamuwa (Mee Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:05:20 | Pitabeddara (Nilwala Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:03:07 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:05:04 | Ellagawa (Kalu Ganga) | 4.99 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:01:55 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:01:35 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:02:22 | Moraketiya (Walawe Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:02:16 | Siyambalanduwa (Heda Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:29:13 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:02:12 | Thaldena (Mahaweli Ganga) | 0.09 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:01:12 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:04:02 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | 0.000 |  |
| 2026-08-19 18:02:30 | Thanthirimale (Malwathu Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:11:33 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:01:11 | Kuda Oya (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-08-20 00:09:23 | Hanwella (Kelani Ganga) | 1.11 | 🟢 Normal | -0.009 |  |
| 2026-08-20 00:01:27 | Nawalapitiya (Mahaweli Ganga) | 1.47 | 🟢 Normal | -0.010 |  |
| 2026-08-19 18:01:56 | Weraganthota (Mahaweli Ganga) | -3.46 | 🟢 Normal | -0.010 |  |
| 2026-08-20 00:12:42 | Magura (Kalu Ganga) | 1.33 | 🟢 Normal | -0.010 |  |
| 2026-08-20 00:06:48 | Baddegama (Gin Ganga) | 1.06 | 🟢 Normal | -0.019 |  |
| 2026-08-20 00:02:54 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.020 |  |
| 2026-08-20 00:00:41 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.032 |  |
| 2026-08-20 00:09:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | -0.047 |  |
| 2026-08-20 00:07:23 | Putupaula (Kalu Ganga) | 0.49 | 🟢 Normal | -0.048 |  |
| 2026-08-20 00:06:36 | Peradeniya (Mahaweli Ganga) | 3.26 | 🟢 Normal | -0.066 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

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

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)