# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--26_06:22:54-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **189,615 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **37** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 06:22:54 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.006 |  |
| 2026-06-26 06:12:38 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:09:01 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.048 |  |
| 2026-06-26 06:08:32 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-26 06:07:51 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-06-26 06:07:23 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-26 06:06:53 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.035 |  |
| 2026-06-26 06:06:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:06:14 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:05:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-06-26 06:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-26 06:05:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 06:05:15 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:05:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.012 |  |
| 2026-06-26 06:04:46 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:04:31 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:04:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:04:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:03:44 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:03:41 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.090 |  |
| 2026-06-26 06:03:26 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.031 |  |
| 2026-06-26 06:03:24 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:03:07 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 06:02:48 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-26 06:02:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:02:08 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-26 06:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:55 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.022 |  |
| 2026-06-26 06:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:27 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 06:01:20 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-26 06:01:19 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:19 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:13 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | -0.021 |  |
| 2026-06-26 06:01:09 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.012 |  |
| 2026-06-26 06:01:02 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.003 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-26 06:05:30 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.80 | 🟢 Normal | 0.209 | 🔺 Rising |
| 2026-06-26 06:07:23 | Hanwella (Kelani Ganga) | 1.85 | 🟢 Normal | 0.027 | 🔺 Rising |
| 2026-06-26 06:01:20 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-26 06:02:48 | Weraganthota (Mahaweli Ganga) | -3.17 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-26 06:03:07 | Dunamale (Aththanagalu Oya) | 1.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-26 06:05:24 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-26 06:01:26 | Wellawaya (Kirindi Oya) | 0.91 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-26 06:02:08 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.007 | 🔺 Rising |
| 2026-06-26 06:02:04 | Kithulgala (Kelani Ganga) | 1.55 | 🟢 Normal | 0.000 |  |
| 2026-06-26 05:02:30 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:27 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:30 | Nawalapitiya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:04:16 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:04:05 | Giriulla (Maha Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:12:38 | Horowpothana (Yan Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:05:15 | Deraniyagala (Kelani Ganga) | 0.81 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:06:22 | Padiyathalawa (Maduru Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:04:31 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:02:10 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:03:44 | Badalgama (Maha Oya) | 2.34 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:04:46 | Holombuwa (Kelani Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:19 | Manampitiya (Mahaweli Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:03:24 | Rathnapura (Kalu Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-06-25 18:02:21 | Thanthirimale (Malwathu Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:06:14 | Urawa (Nilwala Ganga) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:19 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-26 06:01:02 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | -0.003 |  |
| 2026-06-26 06:22:54 | Putupaula (Kalu Ganga) | 0.94 | 🟢 Normal | -0.006 |  |
| 2026-06-26 06:07:51 | Pitabeddara (Nilwala Ganga) | 0.61 | 🟢 Normal | -0.009 |  |
| 2026-06-26 06:08:32 | Thawalama (Gin Ganga) | 1.56 | 🟢 Normal | -0.010 |  |
| 2026-06-26 06:05:15 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | -0.012 |  |
| 2026-06-26 06:01:09 | Panadugama (Nilwala Ganga) | 2.57 | 🟢 Normal | -0.012 |  |
| 2026-06-26 06:01:13 | Glencourse (Kelani Ganga) | 10.02 | 🟢 Normal | -0.021 |  |
| 2026-06-26 06:01:55 | Magura (Kalu Ganga) | 1.67 | 🟢 Normal | -0.022 |  |
| 2026-06-26 06:05:39 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.031 |  |
| 2026-06-26 06:03:26 | Ellagawa (Kalu Ganga) | 5.15 | 🟢 Normal | -0.031 |  |
| 2026-06-26 06:06:53 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | -0.035 |  |
| 2026-06-26 06:09:01 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.048 |  |
| 2026-06-26 06:03:41 | Peradeniya (Mahaweli Ganga) | 1.51 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)