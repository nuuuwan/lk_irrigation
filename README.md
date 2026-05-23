# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_03:31:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,164 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 03:31:14 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.267 |  |
| 2026-05-24 03:26:28 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-05-24 03:14:23 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -36.000 |  |
| 2026-05-24 03:14:21 | Baddegama (Gin Ganga) | 2.08 | 🟢 Normal | -36.000 |  |
| 2026-05-24 03:14:19 | Baddegama (Gin Ganga) | 2.10 | 🟢 Normal | -36.000 |  |
| 2026-05-24 03:11:51 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:10:31 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-05-24 03:09:32 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:09:03 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:08:21 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-05-24 03:06:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 5.976 | 🔺 Rising |
| 2026-05-24 03:06:01 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:05:31 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-24 03:04:46 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.120 |  |
| 2026-05-24 03:04:39 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:04:20 | Hanwella (Kelani Ganga) | 5.20 | 🟢 Normal | -0.097 |  |
| 2026-05-24 03:03:51 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-05-24 03:03:38 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-05-24 03:03:36 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-05-24 03:03:31 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | -0.075 |  |
| 2026-05-24 03:03:29 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:03:28 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | -0.033 |  |
| 2026-05-24 03:03:11 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:03:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:03:08 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.034 |  |
| 2026-05-24 03:02:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:46 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:35 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:16 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.030 |  |
| 2026-05-24 03:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-24 03:02:10 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | 5.976 | 🔺 Rising |
| 2026-05-24 03:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:48 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | -0.076 |  |
| 2026-05-24 03:01:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 03:01:25 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:19 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 02:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-24 03:26:28 | Putupaula (Kalu Ganga) | 3.27 | 🟡 Alert | 0.008 | 🔺 Rising |
| 2026-05-24 03:03:28 | Ellagawa (Kalu Ganga) | 10.14 | 🟡 Alert | -0.033 |  |
| 2026-05-24 03:01:48 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | -0.076 |  |
| 2026-05-24 03:06:23 | Kuda Oya (Kirindi Oya) | 1.35 | 🟢 Normal | 5.976 | 🔺 Rising |
| 2026-05-24 03:05:31 | Deraniyagala (Kelani Ganga) | 1.33 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-05-24 03:01:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 03:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:46 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:19 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:03:11 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:25 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:06:01 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:04:39 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:03:29 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:03:10 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:11:51 | Holombuwa (Kelani Ganga) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:05:55 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:09:32 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:22:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:08:21 | Nawalapitiya (Mahaweli Ganga) | 1.19 | 🟢 Normal | -0.009 |  |
| 2026-05-24 03:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-24 03:03:36 | Panadugama (Nilwala Ganga) | 2.64 | 🟢 Normal | -0.011 |  |
| 2026-05-24 03:03:51 | Moragaswewa (Deduru Oya) | 0.64 | 🟢 Normal | -0.019 |  |
| 2026-05-24 03:10:31 | Thawalama (Gin Ganga) | 1.78 | 🟢 Normal | -0.019 |  |
| 2026-05-24 03:02:16 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.030 |  |
| 2026-05-24 03:03:08 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.034 |  |
| 2026-05-24 03:03:38 | Peradeniya (Mahaweli Ganga) | 1.61 | 🟢 Normal | -0.040 |  |
| 2026-05-24 03:03:31 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | -0.075 |  |
| 2026-05-24 03:04:20 | Hanwella (Kelani Ganga) | 5.20 | 🟢 Normal | -0.097 |  |
| 2026-05-24 03:04:46 | Glencourse (Kelani Ganga) | 11.22 | 🟢 Normal | -0.120 |  |
| 2026-05-24 03:31:14 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.267 |  |
| 2026-05-24 03:14:23 | Baddegama (Gin Ganga) | 2.06 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)