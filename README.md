# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--14_04:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **151,231 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **22** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 04:03:14 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-05-14 04:03:14 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.109 |  |
| 2026-05-14 04:03:03 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:49 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:31 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:07 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.092 |  |
| 2026-05-14 04:01:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:49 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:11 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-14 04:01:11 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.056 |  |
| 2026-05-14 04:01:00 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -1.123 |  |
| 2026-05-14 04:00:53 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-05-14 04:00:21 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:17:51 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-05-14 03:14:42 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-14 03:14:18 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | -0.162 |  |
| 2026-05-14 03:14:14 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | -0.069 |  |
| 2026-05-14 03:12:54 | Nagalagam Street (Kelani Ganga) | 0.91 | 🟢 Normal | -0.109 |  |
| 2026-05-14 03:11:18 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.071 |  |
| 2026-05-14 03:11:12 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.067 |  |
| 2026-05-14 03:10:58 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.014 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-14 03:01:36 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.20 | 🟡 Alert | 0.082 | 🔺 Rising |
| 2026-05-14 03:02:30 | Dunamale (Aththanagalu Oya) | 3.38 | 🟡 Alert | -0.040 |  |
| 2026-05-14 03:14:14 | Magura (Kalu Ganga) | 4.87 | 🟡 Alert | -0.069 |  |
| 2026-05-13 18:02:23 | Galgamuwa (Mee Oya) | 2.97 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-05-14 03:10:58 | Putupaula (Kalu Ganga) | 2.37 | 🟢 Normal | 0.014 | 🔺 Rising |
| 2026-05-14 03:04:58 | Kithulgala (Kelani Ganga) | 1.57 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-13 18:02:22 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-14 03:14:42 | Ellagawa (Kalu Ganga) | 8.27 | 🟢 Normal | 0.008 | 🔺 Rising |
| 2026-05-14 02:00:43 | Thalgahagoda (Nilwala Ganga) | 1.17 | 🟢 Normal | 0.005 | 🔺 Rising |
| 2026-05-14 04:00:21 | Wellawaya (Kirindi Oya) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:00:53 | Nakkala (Kumbukkan Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:07:43 | Moragaswewa (Deduru Oya) | 2.12 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:03:03 | Yaka Wewa (Ma Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:49 | Giriulla (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:51 | Horowpothana (Yan Oya) | 2.05 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:02:31 | Norwood (Kelani Ganga) | 0.83 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:08:01 | Baddegama (Gin Ganga) | 3.28 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:03:58 | Padiyathalawa (Maduru Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:03:28 | Glencourse (Kelani Ganga) | 10.47 | 🟢 Normal | 0.000 |  |
| 2026-05-14 04:01:49 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-05-13 23:06:39 | Katharagama (Menik Ganga) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:05:57 | Thanamalwila (Kirindi Oya) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-05-14 03:03:08 | Kuda Oya (Kirindi Oya) | 1.74 | 🟢 Normal | -0.011 |  |
| 2026-05-14 03:09:31 | Thaldena (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.014 |  |
| 2026-05-14 04:00:35 | Nawalapitiya (Mahaweli Ganga) | 1.22 | 🟢 Normal | -0.022 |  |
| 2026-05-14 04:01:11 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.040 |  |
| 2026-05-14 04:03:14 | Manampitiya (Mahaweli Ganga) | 0.82 | 🟢 Normal | -0.041 |  |
| 2026-05-14 03:09:22 | Deraniyagala (Kelani Ganga) | 0.73 | 🟢 Normal | -0.045 |  |
| 2026-05-13 18:02:14 | Thanthirimale (Malwathu Oya) | 3.35 | 🟢 Normal | -0.051 |  |
| 2026-05-14 03:17:51 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | -0.055 |  |
| 2026-05-14 04:01:11 | Hanwella (Kelani Ganga) | 2.66 | 🟢 Normal | -0.056 |  |
| 2026-05-14 03:07:01 | Urawa (Nilwala Ganga) | 0.55 | 🟢 Normal | -0.063 |  |
| 2026-05-14 02:05:26 | Panadugama (Nilwala Ganga) | 4.79 | 🟢 Normal | -0.065 |  |
| 2026-05-14 03:11:12 | Pitabeddara (Nilwala Ganga) | 1.34 | 🟢 Normal | -0.067 |  |
| 2026-05-14 03:11:18 | Thawalama (Gin Ganga) | 2.63 | 🟢 Normal | -0.071 |  |
| 2026-05-14 04:02:07 | Badalgama (Maha Oya) | 2.84 | 🟢 Normal | -0.092 |  |
| 2026-05-14 04:03:14 | Nagalagam Street (Kelani Ganga) | 0.82 | 🟢 Normal | -0.109 |  |
| 2026-05-14 03:14:18 | Rathnapura (Kalu Ganga) | 5.03 | 🟢 Normal | -0.162 |  |
| 2026-05-14 04:01:00 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -1.123 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)