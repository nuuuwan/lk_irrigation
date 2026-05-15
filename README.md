# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--15_18:11:07-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **152,719 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 18:11:07 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:10:55 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-15 18:10:28 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | -0.058 |  |
| 2026-05-15 18:09:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.086 |  |
| 2026-05-15 18:08:08 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-15 18:05:57 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | -0.022 |  |
| 2026-05-15 18:05:24 | Magura (Kalu Ganga) | 4.29 | 🟡 Alert | -0.051 |  |
| 2026-05-15 18:05:20 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:05:05 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:05:04 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.146 |  |
| 2026-05-15 18:04:42 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:03:51 | Moragaswewa (Deduru Oya) | 3.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 18:03:50 | Giriulla (Maha Oya) | 2.92 | 🟢 Normal | -0.039 |  |
| 2026-05-15 18:03:48 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | -0.062 |  |
| 2026-05-15 18:03:26 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 18:03:21 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:03:20 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:03:14 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 18:02:58 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:02:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-05-15 18:02:53 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:02:37 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:02:32 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.045 |  |
| 2026-05-15 18:02:26 | Dunamale (Aththanagalu Oya) | 4.72 | 🟠 Minor Flood | -0.031 |  |
| 2026-05-15 18:02:12 | Hanwella (Kelani Ganga) | 5.10 | 🟢 Normal | -0.134 |  |
| 2026-05-15 18:01:59 | Rathnapura (Kalu Ganga) | 4.29 | 🟢 Normal | -0.041 |  |
| 2026-05-15 18:01:56 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:39 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:31 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.037 |  |
| 2026-05-15 18:01:17 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 18:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:00:59 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:00:53 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-05-15 18:00:34 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:00:12 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 18:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 18:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-15 18:01:15 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.01 | 🟠 Minor Flood | 0.000 |  |
| 2026-05-15 18:02:26 | Dunamale (Aththanagalu Oya) | 4.72 | 🟠 Minor Flood | -0.031 |  |
| 2026-05-15 18:05:24 | Magura (Kalu Ganga) | 4.29 | 🟡 Alert | -0.051 |  |
| 2026-05-15 18:01:17 | Manampitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | 0.032 | 🔺 Rising |
| 2026-05-15 18:03:02 | Galgamuwa (Mee Oya) | 4.03 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-05-15 18:03:51 | Moragaswewa (Deduru Oya) | 3.98 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-05-15 18:00:10 | Nawalapitiya (Mahaweli Ganga) | 1.52 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-05-15 18:00:12 | Putupaula (Kalu Ganga) | 2.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-05-15 18:03:26 | Norwood (Kelani Ganga) | 0.88 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-15 18:01:07 | Weraganthota (Mahaweli Ganga) | -3.15 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:05:05 | Wellawaya (Kirindi Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:00:34 | Nakkala (Kumbukkan Oya) | 0.91 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:39 | Yaka Wewa (Ma Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:05:20 | Horowpothana (Yan Oya) | 2.98 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:04:42 | Deraniyagala (Kelani Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:02:53 | Ellagawa (Kalu Ganga) | 8.72 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:11:07 | Padiyathalawa (Maduru Oya) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:00:07 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:02:37 | Katharagama (Menik Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:34 | Thanthirimale (Malwathu Oya) | 4.18 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:03:21 | Peradeniya (Mahaweli Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:00:59 | Thalgahagoda (Nilwala Ganga) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:01:56 | Kuda Oya (Kirindi Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:02:58 | Thanamalwila (Kirindi Oya) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-05-15 18:08:08 | Holombuwa (Kelani Ganga) | 1.14 | 🟢 Normal | -0.010 |  |
| 2026-05-15 18:03:14 | Moraketiya (Walawe Ganga) | 1.15 | 🟢 Normal | -0.010 |  |
| 2026-05-15 18:10:55 | Urawa (Nilwala Ganga) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-05-15 18:00:53 | Thaldena (Mahaweli Ganga) | 0.50 | 🟢 Normal | -0.021 |  |
| 2026-05-15 18:05:57 | Baddegama (Gin Ganga) | 3.29 | 🟢 Normal | -0.022 |  |
| 2026-05-15 18:01:31 | Pitabeddara (Nilwala Ganga) | 0.90 | 🟢 Normal | -0.037 |  |
| 2026-05-15 18:03:50 | Giriulla (Maha Oya) | 2.92 | 🟢 Normal | -0.039 |  |
| 2026-05-15 18:01:59 | Rathnapura (Kalu Ganga) | 4.29 | 🟢 Normal | -0.041 |  |
| 2026-05-15 18:02:32 | Thawalama (Gin Ganga) | 2.19 | 🟢 Normal | -0.045 |  |
| 2026-05-15 18:10:28 | Panadugama (Nilwala Ganga) | 4.11 | 🟢 Normal | -0.058 |  |
| 2026-05-15 18:03:48 | Badalgama (Maha Oya) | 4.07 | 🟢 Normal | -0.062 |  |
| 2026-05-15 18:02:58 | Kithulgala (Kelani Ganga) | 1.85 | 🟢 Normal | -0.081 |  |
| 2026-05-15 18:09:41 | Nagalagam Street (Kelani Ganga) | 0.88 | 🟢 Normal | -0.086 |  |
| 2026-05-15 18:02:12 | Hanwella (Kelani Ganga) | 5.10 | 🟢 Normal | -0.134 |  |
| 2026-05-15 18:05:04 | Glencourse (Kelani Ganga) | 11.69 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)