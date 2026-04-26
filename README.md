# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--26_07:01:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **135,304 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 07:01:14 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-26 07:01:04 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:00:39 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-04-26 06:36:45 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-26 06:13:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:12:10 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-26 06:03:27 | Deraniyagala (Kelani Ganga) | 0.26 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-04-26 06:01:45 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.069 | 🔺 Rising |
| 2026-04-26 06:02:11 | Hanwella (Kelani Ganga) | 0.70 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-04-26 06:02:24 | Glencourse (Kelani Ganga) | 8.99 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-26 06:00:57 | Weraganthota (Mahaweli Ganga) | -3.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-26 06:02:19 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:04:02 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:01:29 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:02:46 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:02:20 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:03:44 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:04:17 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:05:16 | Padiyathalawa (Maduru Oya) | 0.18 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:03:05 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:03:24 | Dunamale (Aththanagalu Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:02:30 | Holombuwa (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-04-26 07:01:04 | Thanthirimale (Malwathu Oya) | 1.60 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:13:37 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:02:34 | Thanamalwila (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-26 06:12:10 | Baddegama (Gin Ganga) | 1.03 | 🟢 Normal | -0.009 |  |
| 2026-04-26 06:04:04 | Badalgama (Maha Oya) | 2.07 | 🟢 Normal | -0.010 |  |
| 2026-04-26 06:04:28 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | -0.010 |  |
| 2026-04-26 07:01:14 | Kuda Oya (Kirindi Oya) | 1.51 | 🟢 Normal | -0.010 |  |
| 2026-04-26 06:01:46 | Katharagama (Menik Ganga) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-04-26 06:01:17 | Nawalapitiya (Mahaweli Ganga) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-04-26 06:36:45 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.010 |  |
| 2026-04-26 06:00:42 | Rathnapura (Kalu Ganga) | 0.73 | 🟢 Normal | -0.010 |  |
| 2026-04-26 06:00:55 | Ellagawa (Kalu Ganga) | 4.34 | 🟢 Normal | -0.011 |  |
| 2026-04-26 06:04:24 | Thalgahagoda (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.011 |  |
| 2026-04-26 06:04:07 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.019 |  |
| 2026-04-26 06:00:55 | Moraketiya (Walawe Ganga) | 0.79 | 🟢 Normal | -0.020 |  |
| 2026-04-26 06:05:32 | Magura (Kalu Ganga) | 1.21 | 🟢 Normal | -0.020 |  |
| 2026-04-26 06:01:36 | Moragaswewa (Deduru Oya) | 0.86 | 🟢 Normal | -0.021 |  |
| 2026-04-26 06:02:06 | Thawalama (Gin Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-04-26 07:00:39 | Manampitiya (Mahaweli Ganga) | 0.12 | 🟢 Normal | -0.031 |  |
| 2026-04-26 06:00:38 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.045 |  |
| 2026-04-26 06:06:36 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.055 |  |
| 2026-04-26 06:00:29 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.40 | 🟢 Normal | -0.089 |  |
| 2026-04-26 06:07:52 | Kithulgala (Kelani Ganga) | 1.10 | 🟢 Normal | -0.097 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)