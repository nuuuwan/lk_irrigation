# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--13_18:11:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **72,159 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 18:11:06 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-02-13 18:10:04 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:09:42 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-13 18:07:28 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-02-13 18:07:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-13 18:07:12 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 18:06:12 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:05:40 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 18:05:10 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-13 18:05:07 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -48.000 |  |
| 2026-02-13 18:05:04 | Glencourse (Kelani Ganga) | 8.42 | 🟢 Normal | -48.000 |  |
| 2026-02-13 18:05:02 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.017 |  |
| 2026-02-13 18:04:55 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.040 |  |
| 2026-02-13 18:04:17 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:04:16 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-13 18:03:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:33 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:30 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.045 |  |
| 2026-02-13 18:03:28 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:03:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:02:53 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-13 18:02:25 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-13 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.041 |  |
| 2026-02-13 18:02:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:02:05 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-02-13 18:01:54 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.021 |  |
| 2026-02-13 18:01:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:48 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:35 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.053 |  |
| 2026-02-13 18:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:01:25 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:24 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-13 18:01:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:10 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:07 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:29:40 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.017 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-13 18:02:25 | Manampitiya (Mahaweli Ganga) | 1.40 | 🟢 Normal | 0.092 | 🔺 Rising |
| 2026-02-13 18:05:10 | Horowpothana (Yan Oya) | 1.47 | 🟢 Normal | 0.047 | 🔺 Rising |
| 2026-02-13 18:02:53 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-02-13 18:04:16 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-13 18:07:27 | Nagalagam Street (Kelani Ganga) | 0.40 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-13 18:07:12 | Peradeniya (Mahaweli Ganga) | 1.25 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-13 18:05:40 | Norwood (Kelani Ganga) | 0.43 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-02-13 18:03:51 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:07 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:25 | Moragaswewa (Deduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:04:17 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:50 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 17:02:34 | Panadugama (Nilwala Ganga) | 2.10 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:33 | Siyambalanduwa (Heda Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:45 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:00:10 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:06:12 | Badalgama (Maha Oya) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:11 | Holombuwa (Kelani Ganga) | 0.31 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:03:07 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:48 | Thawalama (Gin Ganga) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:01:48 | Thalgahagoda (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:02:07 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:10:04 | Thanamalwila (Kirindi Oya) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-13 18:09:42 | Katharagama (Menik Ganga) | -0.07 | 🟢 Normal | -0.009 |  |
| 2026-02-13 18:01:24 | Yaka Wewa (Ma Oya) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:03:28 | Hanwella (Kelani Ganga) | 0.41 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:01:25 | Nawalapitiya (Mahaweli Ganga) | 0.72 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:01:12 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | -0.010 |  |
| 2026-02-13 18:05:02 | Magura (Kalu Ganga) | 0.86 | 🟢 Normal | -0.017 |  |
| 2026-02-13 18:11:06 | Urawa (Nilwala Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-02-13 18:07:28 | Dunamale (Aththanagalu Oya) | 0.18 | 🟢 Normal | -0.019 |  |
| 2026-02-13 18:01:54 | Ellagawa (Kalu Ganga) | 4.42 | 🟢 Normal | -0.021 |  |
| 2026-02-13 18:04:55 | Padiyathalawa (Maduru Oya) | 1.05 | 🟢 Normal | -0.040 |  |
| 2026-02-13 18:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.44 | 🟢 Normal | -0.041 |  |
| 2026-02-13 18:03:30 | Rathnapura (Kalu Ganga) | 0.92 | 🟢 Normal | -0.045 |  |
| 2026-02-13 18:01:13 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | -0.050 |  |
| 2026-02-13 18:01:35 | Baddegama (Gin Ganga) | 1.30 | 🟢 Normal | -0.053 |  |
| 2026-02-13 18:02:05 | Kithulgala (Kelani Ganga) | 1.63 | 🟢 Normal | -0.070 |  |
| 2026-02-13 18:05:07 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -48.000 |  |

## River Water Level Charts by Station

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)