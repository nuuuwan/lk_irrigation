# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--26_04:11:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **243,618 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: No active alerts.
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **30** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 04:11:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-08-26 04:09:34 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-26 04:09:31 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.007 |  |
| 2026-08-26 04:09:29 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-26 04:09:19 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-08-26 04:09:17 | Baddegama (Gin Ganga) | 1.49 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-08-26 04:08:49 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 04:07:09 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 04:06:37 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:06:07 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.028 |  |
| 2026-08-26 04:05:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-26 04:05:41 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:05:26 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-08-26 04:05:00 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-26 04:04:53 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:04:10 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:04:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:03:52 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.062 |  |
| 2026-08-26 04:03:40 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.072 |  |
| 2026-08-26 04:03:26 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 04:02:08 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:01:54 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:01:24 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:01:09 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.031 |  |
| 2026-08-26 04:00:57 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-08-26 04:00:48 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:00:39 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-26 03:52:02 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 03:38:54 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-26 03:30:21 | Rathnapura (Kalu Ganga) | 3.47 | 🟢 Normal | 0.205 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-08-26 04:09:19 | Baddegama (Gin Ganga) | 1.57 | 🟢 Normal | 144.000 | 🔺 Rising |
| 2026-08-26 03:04:26 | Panadugama (Nilwala Ganga) | 2.87 | 🟢 Normal | 2.571 | 🔺 Rising |
| 2026-08-26 04:05:26 | Rathnapura (Kalu Ganga) | 3.59 | 🟢 Normal | 0.205 | 🔺 Rising |
| 2026-08-26 04:00:57 | Ellagawa (Kalu Ganga) | 5.97 | 🟢 Normal | 0.172 | 🔺 Rising |
| 2026-08-26 01:09:27 | Pitabeddara (Nilwala Ganga) | 0.88 | 🟢 Normal | 0.170 | 🔺 Rising |
| 2026-08-26 04:11:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.04 | 🟢 Normal | 0.123 | 🔺 Rising |
| 2026-08-26 04:05:00 | Hanwella (Kelani Ganga) | 1.47 | 🟢 Normal | 0.111 | 🔺 Rising |
| 2026-08-26 04:09:29 | Putupaula (Kalu Ganga) | 0.87 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-08-26 04:09:34 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-08-26 04:05:53 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-08-26 02:00:32 | Thawalama (Gin Ganga) | 1.94 | 🟢 Normal | 0.022 | 🔺 Rising |
| 2026-08-26 04:08:49 | Kithulgala (Kelani Ganga) | 1.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-08-26 03:52:02 | Magura (Kalu Ganga) | 2.37 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-08-26 04:03:26 | Badalgama (Maha Oya) | 1.92 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 04:07:09 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-08-26 03:07:32 | Giriulla (Maha Oya) | 0.92 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-08-26 00:02:38 | Wellawaya (Kirindi Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:00:48 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:00:39 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:04:04 | Yaka Wewa (Ma Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:01:54 | Horowpothana (Yan Oya) | 1.82 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:03:25 | Galgamuwa (Mee Oya) | -0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 03:02:52 | Norwood (Kelani Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-08-26 01:12:42 | Padiyathalawa (Maduru Oya) | 0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:01:24 | Siyambalanduwa (Heda Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:04:10 | Dunamale (Aththanagalu Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:05:41 | Thaldena (Mahaweli Ganga) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:04:53 | Katharagama (Menik Ganga) | -0.26 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:06:37 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-08-25 18:02:21 | Thanthirimale (Malwathu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-08-26 03:01:48 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:02:08 | Thanamalwila (Kirindi Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-08-26 04:09:31 | Urawa (Nilwala Ganga) | 0.50 | 🟢 Normal | -0.007 |  |
| 2026-08-25 18:08:33 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.019 |  |
| 2026-08-26 04:06:07 | Manampitiya (Mahaweli Ganga) | 0.00 | 🟢 Normal | -0.028 |  |
| 2026-08-26 04:01:09 | Peradeniya (Mahaweli Ganga) | 2.77 | 🟢 Normal | -0.031 |  |
| 2026-08-26 04:03:52 | Glencourse (Kelani Ganga) | 10.26 | 🟢 Normal | -0.062 |  |
| 2026-08-26 04:03:40 | Deraniyagala (Kelani Ganga) | 1.24 | 🟢 Normal | -0.072 |  |
| 2026-08-26 03:04:11 | Nawalapitiya (Mahaweli Ganga) | 1.64 | 🟢 Normal | -0.077 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)