# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--14_03:06:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **44,970 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **20** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 03:06:08 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.004 |  |
| 2026-01-14 03:06:03 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 03:05:59 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.072 |  |
| 2026-01-14 03:03:59 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:03:30 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-01-14 03:03:24 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:02:26 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:02:20 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:02:07 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:02:03 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-14 03:01:55 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-01-14 03:01:41 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:01:41 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:01:25 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 03:00:47 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-14 03:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 02:58:16 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.062 |  |
| 2026-01-14 02:41:08 | Thalgahagoda (Nilwala Ganga) | 0.52 | 🟢 Normal | -0.072 |  |
| 2026-01-14 02:10:26 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -36.000 |  |
| 2026-01-14 02:10:24 | Pitabeddara (Nilwala Ganga) | 0.70 | 🟢 Normal | -36.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-14 02:02:36 | Hanwella (Kelani Ganga) | 1.01 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-01-14 02:03:22 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-01-14 03:00:47 | Dunamale (Aththanagalu Oya) | 1.26 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-01-14 01:03:40 | Glencourse (Kelani Ganga) | 9.00 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-14 01:06:49 | Putupaula (Kalu Ganga) | 0.44 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-01-14 00:07:06 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-01-14 03:06:03 | Thanamalwila (Kirindi Oya) | 1.03 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 03:01:25 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 02:05:31 | Rathnapura (Kalu Ganga) | 0.68 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-14 03:06:08 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.004 |  |
| 2026-01-14 03:02:20 | Wellawaya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:01:41 | Nakkala (Kumbukkan Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:00:22 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 02:03:36 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-13 18:03:54 | Galgamuwa (Mee Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:03:59 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:01:41 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 00:28:08 | Baddegama (Gin Ganga) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:02:07 | Padiyathalawa (Maduru Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-14 02:04:09 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-01-14 02:04:54 | Thaldena (Mahaweli Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-14 02:02:11 | Katharagama (Menik Ganga) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:03:24 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-01-14 01:17:13 | Holombuwa (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-01-14 03:02:26 | Thawalama (Gin Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-01-14 02:04:21 | Urawa (Nilwala Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-01-14 02:01:41 | Kuda Oya (Kirindi Oya) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-01-14 01:10:35 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | -0.009 |  |
| 2026-01-14 03:02:03 | Moragaswewa (Deduru Oya) | 0.60 | 🟢 Normal | -0.010 |  |
| 2026-01-14 03:01:55 | Yaka Wewa (Ma Oya) | 1.09 | 🟢 Normal | -0.011 |  |
| 2026-01-14 02:01:40 | Siyambalanduwa (Heda Oya) | 0.98 | 🟢 Normal | -0.012 |  |
| 2026-01-14 03:03:30 | Manampitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -0.019 |  |
| 2026-01-13 18:03:19 | Thanthirimale (Malwathu Oya) | 2.59 | 🟢 Normal | -0.020 |  |
| 2026-01-13 18:01:14 | Weraganthota (Mahaweli Ganga) | -1.58 | 🟢 Normal | -0.040 |  |
| 2026-01-14 02:58:16 | Peradeniya (Mahaweli Ganga) | 2.21 | 🟢 Normal | -0.062 |  |
| 2026-01-14 03:05:59 | Thalgahagoda (Nilwala Ganga) | 0.49 | 🟢 Normal | -0.072 |  |
| 2026-01-14 01:04:15 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.091 |  |
| 2026-01-14 01:02:38 | Horowpothana (Yan Oya) | 3.70 | 🟢 Normal | -0.097 |  |
| 2026-01-14 02:10:26 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)