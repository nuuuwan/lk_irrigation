# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--15_23:20:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **74,117 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 23:20:16 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.034 |  |
| 2026-02-15 23:12:56 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:12:40 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:12:07 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-02-15 23:10:41 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:08:59 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.060 |  |
| 2026-02-15 23:08:53 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-15 23:07:37 | Norwood (Kelani Ganga) | 4.20 | 🟠 Minor Flood | 3.547 | 🔺 Rising |
| 2026-02-15 23:07:24 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:07:15 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:07:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:06:35 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 23:05:31 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-15 23:05:08 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:04:45 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:04:39 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-02-15 23:04:26 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:04:22 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:03:47 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-02-15 23:03:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:02:31 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:02:18 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:02:07 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-15 23:01:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-15 23:01:20 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:01:13 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-02-15 23:01:09 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-15 23:01:01 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-02-15 23:00:58 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-02-15 23:00:34 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 23:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:00:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 22:59:30 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 22:30:19 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 22:26:41 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-15 23:07:37 | Norwood (Kelani Ganga) | 4.20 | 🟠 Minor Flood | 3.547 | 🔺 Rising |
| 2026-02-15 23:01:13 | Kithulgala (Kelani Ganga) | 1.50 | 🟢 Normal | 0.254 | 🔺 Rising |
| 2026-02-15 23:05:31 | Peradeniya (Mahaweli Ganga) | 1.54 | 🟢 Normal | 0.116 | 🔺 Rising |
| 2026-02-15 23:01:46 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | 0.070 | 🔺 Rising |
| 2026-02-15 23:08:53 | Glencourse (Kelani Ganga) | 8.33 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-02-15 23:06:35 | Thanamalwila (Kirindi Oya) | 0.56 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-02-15 23:00:34 | Wellawaya (Kirindi Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-15 22:02:51 | Moragaswewa (Deduru Oya) | 0.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:00:28 | Nawalapitiya (Mahaweli Ganga) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:12:40 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:04:22 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-02-15 22:00:43 | Horowpothana (Yan Oya) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:02:48 | Galgamuwa (Mee Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:04:45 | Pitabeddara (Nilwala Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:01:20 | Baddegama (Gin Ganga) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:10:41 | Panadugama (Nilwala Ganga) | 2.04 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:02:18 | Padiyathalawa (Maduru Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:00:10 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:03:36 | Siyambalanduwa (Heda Oya) | 0.53 | 🟢 Normal | 0.000 |  |
| 2026-02-15 22:26:41 | Dunamale (Aththanagalu Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:05:08 | Katharagama (Menik Ganga) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:07:15 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:07:12 | Holombuwa (Kelani Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:04:26 | Rathnapura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-02-15 18:01:14 | Thanthirimale (Malwathu Oya) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:07:24 | Thawalama (Gin Ganga) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:12:56 | Urawa (Nilwala Ganga) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:02:31 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-02-15 23:02:07 | Nakkala (Kumbukkan Oya) | 0.85 | 🟢 Normal | -0.010 |  |
| 2026-02-15 23:00:58 | Ellagawa (Kalu Ganga) | 4.14 | 🟢 Normal | -0.010 |  |
| 2026-02-15 23:01:09 | Thaldena (Mahaweli Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-02-15 23:04:39 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | -0.019 |  |
| 2026-02-15 23:12:07 | Magura (Kalu Ganga) | 1.08 | 🟢 Normal | -0.019 |  |
| 2026-02-15 23:03:47 | Hanwella (Kelani Ganga) | 0.39 | 🟢 Normal | -0.020 |  |
| 2026-02-15 21:04:24 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.88 | 🟢 Normal | -0.023 |  |
| 2026-02-15 23:20:16 | Thalgahagoda (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.034 |  |
| 2026-02-15 23:01:01 | Manampitiya (Mahaweli Ganga) | 1.75 | 🟢 Normal | -0.050 |  |
| 2026-02-15 23:08:59 | Putupaula (Kalu Ganga) | 0.41 | 🟢 Normal | -0.060 |  |
| 2026-02-15 18:00:16 | Weraganthota (Mahaweli Ganga) | -2.47 | 🟢 Normal | -0.064 |  |

## River Water Level Charts by Station

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)