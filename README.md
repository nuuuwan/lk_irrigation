# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--12_11:11:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **285,796 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟡 Kalawellawa (Millakanda) — Alert
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 11:11:48 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:11:16 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.101 |  |
| 2026-10-12 11:10:21 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.086 |  |
| 2026-10-12 11:10:20 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:08:00 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:07:52 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.032 |  |
| 2026-10-12 11:07:45 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:06:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-12 11:06:45 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:06:29 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-10-12 11:06:27 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.079 |  |
| 2026-10-12 11:05:53 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.048 |  |
| 2026-10-12 11:05:40 | Dunamale (Aththanagalu Oya) | 2.79 | 🟢 Normal | -0.021 |  |
| 2026-10-12 11:05:31 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-10-12 11:05:26 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:05:10 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.151 |  |
| 2026-10-12 11:04:47 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:04:39 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.071 |  |
| 2026-10-12 11:04:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 11:03:55 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:03:38 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 11:03:25 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 11:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.020 |  |
| 2026-10-12 11:03:04 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.070 |  |
| 2026-10-12 11:02:48 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-10-12 11:02:29 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:02:18 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-12 11:02:16 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.133 |  |
| 2026-10-12 11:02:15 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:02:09 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-12 11:02:06 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:02:01 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.056 |  |
| 2026-10-12 11:01:56 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-12 11:01:32 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:01:08 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:01:00 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-12 11:03:17 | Kalawellawa (Millakanda) (Kalu Ganga) | 5.12 | 🟡 Alert | -0.020 |  |
| 2026-10-12 11:06:46 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.085 | 🔺 Rising |
| 2026-10-12 11:02:09 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-12 11:03:25 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 11:04:14 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-12 11:07:45 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:08:00 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:01:02 | Horowpothana (Yan Oya) | 1.61 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:02:29 | Galgamuwa (Mee Oya) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:05:26 | Deraniyagala (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:10:20 | Baddegama (Gin Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:01:08 | Padiyathalawa (Maduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:02:06 | Katharagama (Menik Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:11:48 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-10-12 11:01:56 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-12 11:01:00 | Weraganthota (Mahaweli Ganga) | -3.22 | 🟢 Normal | -0.010 |  |
| 2026-10-12 11:03:38 | Ellagawa (Kalu Ganga) | 7.26 | 🟢 Normal | -0.010 |  |
| 2026-10-12 11:02:48 | Norwood (Kelani Ganga) | 0.99 | 🟢 Normal | -0.011 |  |
| 2026-10-12 11:05:31 | Thalgahagoda (Nilwala Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-10-12 11:04:47 | Kuda Oya (Kirindi Oya) | 1.42 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:03:55 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:02:15 | Thanamalwila (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:01:32 | Pitabeddara (Nilwala Ganga) | 1.58 | 🟢 Normal | -0.020 |  |
| 2026-10-12 11:06:45 | Putupaula (Kalu Ganga) | 1.70 | 🟢 Normal | -0.020 |  |
| 2026-10-12 10:01:53 | Moragaswewa (Deduru Oya) | 1.01 | 🟢 Normal | -0.021 |  |
| 2026-10-12 11:05:40 | Dunamale (Aththanagalu Oya) | 2.79 | 🟢 Normal | -0.021 |  |
| 2026-10-12 11:02:18 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.030 |  |
| 2026-10-12 11:07:52 | Holombuwa (Kelani Ganga) | 1.04 | 🟢 Normal | -0.032 |  |
| 2026-10-12 11:06:29 | Giriulla (Maha Oya) | 2.24 | 🟢 Normal | -0.037 |  |
| 2026-10-12 11:05:53 | Glencourse (Kelani Ganga) | 11.17 | 🟢 Normal | -0.048 |  |
| 2026-10-12 11:02:01 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | -0.056 |  |
| 2026-10-12 11:03:04 | Hanwella (Kelani Ganga) | 3.53 | 🟢 Normal | -0.070 |  |
| 2026-10-12 11:04:39 | Kithulgala (Kelani Ganga) | 2.03 | 🟢 Normal | -0.071 |  |
| 2026-10-12 10:15:09 | Urawa (Nilwala Ganga) | 1.09 | 🟢 Normal | -0.076 |  |
| 2026-10-12 11:06:27 | Badalgama (Maha Oya) | 3.59 | 🟢 Normal | -0.079 |  |
| 2026-10-12 11:10:21 | Panadugama (Nilwala Ganga) | 4.68 | 🟢 Normal | -0.086 |  |
| 2026-10-12 11:11:16 | Peradeniya (Mahaweli Ganga) | 2.62 | 🟢 Normal | -0.101 |  |
| 2026-10-12 11:02:16 | Magura (Kalu Ganga) | 2.56 | 🟢 Normal | -0.133 |  |
| 2026-10-12 11:05:10 | Rathnapura (Kalu Ganga) | 2.82 | 🟢 Normal | -0.151 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)