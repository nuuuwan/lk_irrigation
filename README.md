# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_00:01:48-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,992 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **12** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 00:01:48 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:26 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:18 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:00:56 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:00:38 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-05-14 23:27:37 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.007 |  |
| 2026-05-14 23:15:48 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-05-14 23:12:51 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-05-14 23:12:25 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:10:24 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:08:22 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 23:05:09 | Dunamale (Aththanagalu Oya) | 4.40 | 🟠 Minor Flood | 0.094 | 🔺 Rising |
| 2026-05-14 23:03:19 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.62 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-14 23:03:40 | Magura (Kalu Ganga) | 4.99 | 🟡 Alert | -0.019 |  |
| 2026-05-14 23:05:51 | Glencourse (Kelani Ganga) | 14.10 | 🟢 Normal | 0.158 | 🔺 Rising |
| 2026-05-14 23:03:10 | Hanwella (Kelani Ganga) | 5.21 | 🟢 Normal | 0.145 | 🔺 Rising |
| 2026-05-14 23:05:13 | Badalgama (Maha Oya) | 4.40 | 🟢 Normal | 0.135 | 🔺 Rising |
| 2026-05-14 23:04:21 | Nagalagam Street (Kelani Ganga) | 0.79 | 🟢 Normal | 0.062 | 🔺 Rising |
| 2026-05-14 23:07:12 | Thawalama (Gin Ganga) | 2.34 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-05-14 23:02:12 | Giriulla (Maha Oya) | 3.83 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-05-14 23:04:06 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | 0.048 | 🔺 Rising |
| 2026-05-14 23:02:21 | Pitabeddara (Nilwala Ganga) | 1.14 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-05-14 23:04:59 | Norwood (Kelani Ganga) | 1.05 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 23:06:37 | Ellagawa (Kalu Ganga) | 8.56 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 18:00:44 | Weraganthota (Mahaweli Ganga) | -3.08 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:48 | Wellawaya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:10:24 | Moragaswewa (Deduru Oya) | 1.58 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:01:28 | Horowpothana (Yan Oya) | 2.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:06:18 | Baddegama (Gin Ganga) | 3.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:28 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:00:56 | Siyambalanduwa (Heda Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:05:20 | Katharagama (Menik Ganga) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-05-14 18:03:16 | Thanthirimale (Malwathu Oya) | 3.25 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:12:25 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 00:01:18 | Kuda Oya (Kirindi Oya) | 1.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 23:27:37 | Moraketiya (Walawe Ganga) | 1.17 | 🟢 Normal | -0.007 |  |
| 2026-05-14 23:15:48 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.009 |  |
| 2026-05-14 23:12:51 | Putupaula (Kalu Ganga) | 2.59 | 🟢 Normal | -0.009 |  |
| 2026-05-14 23:06:33 | Thanamalwila (Kirindi Oya) | 1.44 | 🟢 Normal | -0.010 |  |
| 2026-05-14 23:02:07 | Manampitiya (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.012 |  |
| 2026-05-14 23:07:38 | Panadugama (Nilwala Ganga) | 3.71 | 🟢 Normal | -0.019 |  |
| 2026-05-14 23:04:04 | Kithulgala (Kelani Ganga) | 2.08 | 🟢 Normal | -0.022 |  |
| 2026-05-14 23:04:39 | Rathnapura (Kalu Ganga) | 4.92 | 🟢 Normal | -0.030 |  |
| 2026-05-14 23:01:54 | Yaka Wewa (Ma Oya) | 0.95 | 🟢 Normal | -0.030 |  |
| 2026-05-15 00:00:38 | Thaldena (Mahaweli Ganga) | 0.62 | 🟢 Normal | -0.030 |  |
| 2026-05-14 23:07:34 | Holombuwa (Kelani Ganga) | 1.66 | 🟢 Normal | -0.060 |  |
| 2026-05-14 22:06:29 | Nawalapitiya (Mahaweli Ganga) | 1.91 | 🟢 Normal | -0.075 |  |
| 2026-05-14 23:02:59 | Peradeniya (Mahaweli Ganga) | 1.82 | 🟢 Normal | -0.086 |  |
| 2026-05-14 18:05:46 | Galgamuwa (Mee Oya) | 1.40 | 🟢 Normal | -0.087 |  |
| 2026-05-14 23:04:02 | Deraniyagala (Kelani Ganga) | 2.27 | 🟢 Normal | -0.142 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)