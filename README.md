# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--10--20_08:23:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **292,908 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

🇱🇰 River water alerts: 🟠 Thalgahagoda — Minor Flood
Source: Sri Lanka Irrigation Department https://www.irrigation.gov.lk
Repo: https://github.com/nuuuwan/lk_irrigation
## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 08:23:51 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:15:42 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:12:28 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:11:48 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.017 |  |
| 2026-10-20 08:08:29 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.018 |  |
| 2026-10-20 08:08:12 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:07:35 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:06:41 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:06:36 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:06:11 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-10-20 08:06:01 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-10-20 08:05:40 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:05:24 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.042 |  |
| 2026-10-20 08:04:58 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.090 |  |
| 2026-10-20 08:04:54 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 08:04:33 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.012 |  |
| 2026-10-20 08:04:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:03:56 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 08:03:27 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-20 08:03:25 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-20 08:03:16 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:03:10 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:03:02 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:02:57 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 08:02:52 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.061 |  |
| 2026-10-20 08:02:47 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-20 08:02:31 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-20 08:02:25 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:02:22 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.040 |  |
| 2026-10-20 08:02:01 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:01:55 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:01:47 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 08:01:41 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.020 |  |
| 2026-10-20 08:01:40 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:01:33 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | -0.061 |  |
| 2026-10-20 08:01:28 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 08:01:27 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.022 |  |
| 2026-10-20 08:01:13 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.085 |  |
| 2026-10-20 08:00:53 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.103 |  |
| 2026-10-20 08:00:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.016 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-10-20 08:08:29 | Thalgahagoda (Nilwala Ganga) | 1.72 | 🟠 Minor Flood | -0.018 |  |
| 2026-10-20 08:03:25 | Siyambalanduwa (Heda Oya) | 0.59 | 🟢 Normal | 0.049 | 🔺 Rising |
| 2026-10-20 08:01:28 | Thaldena (Mahaweli Ganga) | 0.31 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-10-20 08:02:31 | Peradeniya (Mahaweli Ganga) | 2.82 | 🟢 Normal | 0.034 | 🔺 Rising |
| 2026-10-20 08:04:54 | Thawalama (Gin Ganga) | 2.20 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-10-20 08:02:57 | Wellawaya (Kirindi Oya) | 1.36 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 08:03:56 | Putupaula (Kalu Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 08:01:47 | Kithulgala (Kelani Ganga) | 2.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-10-20 08:12:28 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:08:12 | Giriulla (Maha Oya) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:06:41 | Galgamuwa (Mee Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:03:10 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:03:02 | Moraketiya (Walawe Ganga) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:02:25 | Dunamale (Aththanagalu Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:15:42 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:23:51 | Urawa (Nilwala Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:07:35 | Kuda Oya (Kirindi Oya) | 1.39 | 🟢 Normal | 0.000 |  |
| 2026-10-20 08:06:11 | Pitabeddara (Nilwala Ganga) | 1.51 | 🟢 Normal | -0.009 |  |
| 2026-10-20 08:04:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.27 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:01:55 | Yaka Wewa (Ma Oya) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:05:40 | Badalgama (Maha Oya) | 2.64 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:02:01 | Thanthirimale (Malwathu Oya) | 1.31 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:03:16 | Hanwella (Kelani Ganga) | 2.99 | 🟢 Normal | -0.010 |  |
| 2026-10-20 07:06:24 | Holombuwa (Kelani Ganga) | 0.84 | 🟢 Normal | -0.010 |  |
| 2026-10-20 08:03:27 | Norwood (Kelani Ganga) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-10-20 08:06:01 | Magura (Kalu Ganga) | 1.84 | 🟢 Normal | -0.012 |  |
| 2026-10-20 08:04:33 | Baddegama (Gin Ganga) | 2.05 | 🟢 Normal | -0.012 |  |
| 2026-10-20 08:00:19 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.016 |  |
| 2026-10-20 08:11:48 | Horowpothana (Yan Oya) | 2.26 | 🟢 Normal | -0.017 |  |
| 2026-10-20 08:02:47 | Manampitiya (Mahaweli Ganga) | 0.36 | 🟢 Normal | -0.020 |  |
| 2026-10-20 08:01:41 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | -0.020 |  |
| 2026-10-20 08:01:27 | Moragaswewa (Deduru Oya) | 1.14 | 🟢 Normal | -0.022 |  |
| 2026-10-20 08:02:22 | Thanamalwila (Kirindi Oya) | 1.31 | 🟢 Normal | -0.040 |  |
| 2026-10-20 08:05:24 | Rathnapura (Kalu Ganga) | 2.40 | 🟢 Normal | -0.042 |  |
| 2026-10-20 08:01:33 | Panadugama (Nilwala Ganga) | 4.73 | 🟢 Normal | -0.061 |  |
| 2026-10-20 08:02:52 | Deraniyagala (Kelani Ganga) | 0.95 | 🟢 Normal | -0.061 |  |
| 2026-10-20 08:01:13 | Nakkala (Kumbukkan Oya) | 1.16 | 🟢 Normal | -0.085 |  |
| 2026-10-20 08:04:58 | Glencourse (Kelani Ganga) | 11.06 | 🟢 Normal | -0.090 |  |
| 2026-10-20 08:00:53 | Weraganthota (Mahaweli Ganga) | -3.03 | 🟢 Normal | -0.103 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)