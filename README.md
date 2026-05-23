# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--24_03:02:51-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **160,139 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **17** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 03:02:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:46 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:35 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:16 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.030 |  |
| 2026-05-24 03:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-24 03:02:10 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.404 |  |
| 2026-05-24 03:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:48 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | -0.076 |  |
| 2026-05-24 03:01:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 03:01:25 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:19 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:34:23 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:24:38 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.043 |  |
| 2026-05-24 02:14:57 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.026 |  |
| 2026-05-24 02:14:35 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.008 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-24 02:03:27 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.67 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-24 01:04:10 | Putupaula (Kalu Ganga) | 3.25 | 🟡 Alert | 0.011 | 🔺 Rising |
| 2026-05-24 02:09:07 | Ellagawa (Kalu Ganga) | 10.17 | 🟡 Alert | 0.000 |  |
| 2026-05-24 03:01:48 | Dunamale (Aththanagalu Oya) | 4.30 | 🟡 Alert | -0.076 |  |
| 2026-05-24 02:04:00 | Peradeniya (Mahaweli Ganga) | 1.65 | 🟢 Normal | 1706.400 | 🔺 Rising |
| 2026-05-24 03:01:25 | Moraketiya (Walawe Ganga) | 0.95 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-23 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-24 03:02:04 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:46 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:34 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:51 | Yaka Wewa (Ma Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:19 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:00:44 | Horowpothana (Yan Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-05-23 18:04:23 | Galgamuwa (Mee Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:01:25 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:05:41 | Norwood (Kelani Ganga) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:07:53 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:02:36 | Padiyathalawa (Maduru Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:05:52 | Siyambalanduwa (Heda Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:01 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-24 03:02:35 | Katharagama (Menik Ganga) | -0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:05:55 | Manampitiya (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-05-24 00:22:42 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-24 02:14:35 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.008 |  |
| 2026-05-24 03:02:11 | Thanamalwila (Kirindi Oya) | 0.69 | 🟢 Normal | -0.010 |  |
| 2026-05-23 18:01:26 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-05-24 02:04:24 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.012 |  |
| 2026-05-24 02:08:23 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.019 |  |
| 2026-05-24 02:00:23 | Moragaswewa (Deduru Oya) | 0.66 | 🟢 Normal | -0.021 |  |
| 2026-05-24 02:01:56 | Holombuwa (Kelani Ganga) | 0.52 | 🟢 Normal | -0.022 |  |
| 2026-05-24 02:14:57 | Hanwella (Kelani Ganga) | 5.28 | 🟢 Normal | -0.026 |  |
| 2026-05-24 03:02:16 | Badalgama (Maha Oya) | 2.80 | 🟢 Normal | -0.030 |  |
| 2026-05-24 02:01:32 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | -0.040 |  |
| 2026-05-24 00:05:10 | Baddegama (Gin Ganga) | 2.14 | 🟢 Normal | -0.040 |  |
| 2026-05-24 02:24:38 | Glencourse (Kelani Ganga) | 11.30 | 🟢 Normal | -0.043 |  |
| 2026-05-24 02:01:12 | Magura (Kalu Ganga) | 2.70 | 🟢 Normal | -0.051 |  |
| 2026-05-24 02:09:45 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | -0.056 |  |
| 2026-05-24 01:03:05 | Rathnapura (Kalu Ganga) | 5.07 | 🟢 Normal | -0.071 |  |
| 2026-05-24 03:02:10 | Kuda Oya (Kirindi Oya) | 0.93 | 🟢 Normal | -0.404 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)