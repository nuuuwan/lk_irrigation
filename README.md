# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--25_03:47:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **134,291 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **7** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 03:47:53 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 03:43:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:30:57 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:30:21 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:16:58 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-04-25 03:12:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:11:12 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-25 01:08:46 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | 21.545 | 🔺 Rising |
| 2026-04-25 03:04:25 | Wellawaya (Kirindi Oya) | 1.01 | 🟢 Normal | 0.174 | 🔺 Rising |
| 2026-04-25 03:06:56 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-25 03:47:53 | Putupaula (Kalu Ganga) | 0.54 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-25 03:06:38 | Kuda Oya (Kirindi Oya) | 1.73 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-04-25 03:03:10 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-24 18:01:26 | Thanthirimale (Malwathu Oya) | 2.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-25 03:00:54 | Nakkala (Kumbukkan Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:12:40 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:01:32 | Horowpothana (Yan Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-04-24 18:01:28 | Galgamuwa (Mee Oya) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:03:33 | Deraniyagala (Kelani Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:02:27 | Padiyathalawa (Maduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:04:49 | Glencourse (Kelani Ganga) | 9.10 | 🟢 Normal | 0.000 |  |
| 2026-04-25 01:00:11 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:43:49 | Siyambalanduwa (Heda Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:02:24 | Manampitiya (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:30:57 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-04-25 03:07:03 | Thanamalwila (Kirindi Oya) | 1.42 | 🟢 Normal | -0.006 |  |
| 2026-04-25 03:11:12 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | -0.009 |  |
| 2026-04-25 03:03:22 | Moragaswewa (Deduru Oya) | 0.95 | 🟢 Normal | -0.010 |  |
| 2026-04-25 03:03:52 | Katharagama (Menik Ganga) | 1.79 | 🟢 Normal | -0.010 |  |
| 2026-04-25 03:02:25 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.010 |  |
| 2026-04-25 03:16:58 | Pitabeddara (Nilwala Ganga) | 0.73 | 🟢 Normal | -0.018 |  |
| 2026-04-25 03:04:05 | Magura (Kalu Ganga) | 1.46 | 🟢 Normal | -0.019 |  |
| 2026-04-25 03:07:09 | Rathnapura (Kalu Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-04-25 03:04:30 | Badalgama (Maha Oya) | 2.37 | 🟢 Normal | -0.020 |  |
| 2026-04-25 01:20:11 | Panadugama (Nilwala Ganga) | 3.00 | 🟢 Normal | -0.021 |  |
| 2026-04-25 03:05:50 | Thaldena (Mahaweli Ganga) | 0.33 | 🟢 Normal | -0.028 |  |
| 2026-04-24 18:04:10 | Weraganthota (Mahaweli Ganga) | -3.19 | 🟢 Normal | -0.028 |  |
| 2026-04-25 03:05:58 | Holombuwa (Kelani Ganga) | 0.45 | 🟢 Normal | -0.030 |  |
| 2026-04-25 03:04:22 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | -0.031 |  |
| 2026-04-25 03:02:21 | Hanwella (Kelani Ganga) | 1.08 | 🟢 Normal | -0.034 |  |
| 2026-04-25 02:04:07 | Dunamale (Aththanagalu Oya) | 1.14 | 🟢 Normal | -0.040 |  |
| 2026-04-25 03:01:19 | Ellagawa (Kalu Ganga) | 4.90 | 🟢 Normal | -0.041 |  |
| 2026-04-25 03:06:02 | Kithulgala (Kelani Ganga) | 1.13 | 🟢 Normal | -0.074 |  |
| 2026-04-25 03:01:16 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | -0.076 |  |
| 2026-04-25 02:06:05 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.74 | 🟢 Normal | -0.083 |  |

## River Water Level Charts by Station

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)