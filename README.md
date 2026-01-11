# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--01--11_12:10:13-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **42,670 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **42** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 12:10:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.056 |  |
| 2026-01-11 12:09:21 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:07:48 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-11 12:06:32 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:05:59 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 12:05:37 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-01-11 12:05:35 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:05:34 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:05:13 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:04:56 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-01-11 12:04:56 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:04:07 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-01-11 12:03:55 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 12:03:53 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:44 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:30 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:30 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-11 12:03:28 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:17 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-01-11 12:03:14 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:09 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-11 12:03:09 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:52 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.111 |  |
| 2026-01-11 12:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:32 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:28 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:26 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.315 |  |
| 2026-01-11 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:07 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:05 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:41 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:37 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.022 |  |
| 2026-01-11 12:01:18 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:13 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-11 12:01:12 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.088 |  |
| 2026-01-11 12:01:12 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 12:01:07 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:00:33 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:00:13 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:36:21 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 11:25:33 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-01-11 12:01:12 | Kithulgala (Kelani Ganga) | 1.48 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-01-11 12:03:55 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 12:05:59 | Padiyathalawa (Maduru Oya) | 1.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-01-11 12:02:07 | Weraganthota (Mahaweli Ganga) | -1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:41 | Wellawaya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:00:33 | Nakkala (Kumbukkan Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:39 | Nawalapitiya (Mahaweli Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:18 | Yaka Wewa (Ma Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:06:32 | Galgamuwa (Mee Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:53 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:28 | Pitabeddara (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:05:35 | Norwood (Kelani Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:07 | Ellagawa (Kalu Ganga) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:32 | Panadugama (Nilwala Ganga) | 2.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:28 | Glencourse (Kelani Ganga) | 8.67 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:01:46 | Moraketiya (Walawe Ganga) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:00:13 | Siyambalanduwa (Heda Oya) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:09 | Dunamale (Aththanagalu Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:05:34 | Thaldena (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:44 | Badalgama (Maha Oya) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:05:13 | Holombuwa (Kelani Ganga) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:30 | Thanthirimale (Malwathu Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:03:14 | Urawa (Nilwala Ganga) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:05 | Kuda Oya (Kirindi Oya) | 1.31 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:09:21 | Thanamalwila (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:02:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | 0.000 |  |
| 2026-01-11 12:05:37 | Moragaswewa (Deduru Oya) | 0.55 | 🟢 Normal | -0.009 |  |
| 2026-01-11 12:07:48 | Giriulla (Maha Oya) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-01-11 12:03:09 | Rathnapura (Kalu Ganga) | 0.78 | 🟢 Normal | -0.010 |  |
| 2026-01-11 12:03:30 | Hanwella (Kelani Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-01-11 12:01:13 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.011 |  |
| 2026-01-11 12:04:56 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.020 |  |
| 2026-01-11 12:04:07 | Horowpothana (Yan Oya) | 2.53 | 🟢 Normal | -0.020 |  |
| 2026-01-11 12:01:37 | Thawalama (Gin Ganga) | 1.25 | 🟢 Normal | -0.022 |  |
| 2026-01-11 12:03:17 | Putupaula (Kalu Ganga) | 0.36 | 🟢 Normal | -0.040 |  |
| 2026-01-11 12:10:13 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | -0.056 |  |
| 2026-01-11 12:01:12 | Peradeniya (Mahaweli Ganga) | 1.70 | 🟢 Normal | -0.088 |  |
| 2026-01-11 12:02:52 | Deraniyagala (Kelani Ganga) | 0.21 | 🟢 Normal | -0.111 |  |
| 2026-01-11 12:02:26 | Manampitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | -0.315 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)