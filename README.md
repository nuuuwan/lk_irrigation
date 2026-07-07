# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--07--08_03:15:28-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **200,271 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 03:15:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-07-08 03:12:40 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.017 |  |
| 2026-07-08 03:12:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-07-08 03:09:19 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.012 |  |
| 2026-07-08 03:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:08:21 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-07-08 02:05:18 | Glencourse (Kelani Ganga) | 9.67 | 🟢 Normal | 0.099 | 🔺 Rising |
| 2026-07-08 03:02:38 | Nagalagam Street (Kelani Ganga) | 0.46 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-07-08 02:11:40 | Putupaula (Kalu Ganga) | 0.52 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-07-08 03:01:25 | Manampitiya (Mahaweli Ganga) | -0.15 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-07-08 03:04:10 | Moraketiya (Walawe Ganga) | 0.77 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 03:02:56 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-07-08 03:04:26 | Thaldena (Mahaweli Ganga) | 0.11 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-07-07 18:04:20 | Weraganthota (Mahaweli Ganga) | -3.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:00:21 | Wellawaya (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:01:16 | Nakkala (Kumbukkan Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:01:46 | Moragaswewa (Deduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:00:29 | Nawalapitiya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:01:55 | Yaka Wewa (Ma Oya) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:02:11 | Giriulla (Maha Oya) | 1.05 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:01:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:03:00 | Galgamuwa (Mee Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:06:12 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:02:08 | Hanwella (Kelani Ganga) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:05:01 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:05:27 | Panadugama (Nilwala Ganga) | 2.19 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:02:59 | Padiyathalawa (Maduru Oya) | 0.06 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:01:26 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:02:17 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:03:09 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:03:24 | Badalgama (Maha Oya) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:08:21 | Rathnapura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-07-07 18:01:02 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-07-08 02:03:39 | Urawa (Nilwala Ganga) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:05:38 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-08 02:06:53 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:05:37 | Thanamalwila (Kirindi Oya) | 0.20 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:08:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.50 | 🟢 Normal | 0.000 |  |
| 2026-07-08 03:15:28 | Kithulgala (Kelani Ganga) | 1.56 | 🟢 Normal | -0.009 |  |
| 2026-07-08 03:12:27 | Holombuwa (Kelani Ganga) | 0.50 | 🟢 Normal | -0.009 |  |
| 2026-07-08 03:01:47 | Thawalama (Gin Ganga) | 1.22 | 🟢 Normal | -0.010 |  |
| 2026-07-08 03:09:19 | Ellagawa (Kalu Ganga) | 4.59 | 🟢 Normal | -0.012 |  |
| 2026-07-08 03:12:40 | Deraniyagala (Kelani Ganga) | 0.63 | 🟢 Normal | -0.017 |  |
| 2026-07-08 03:04:57 | Peradeniya (Mahaweli Ganga) | 2.08 | 🟢 Normal | -0.094 |  |
| 2026-07-08 02:11:10 | Magura (Kalu Ganga) | 1.05 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)