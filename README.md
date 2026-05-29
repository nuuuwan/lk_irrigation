# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--05--29_23:24:01-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **165,210 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **35** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 23:24:01 | Rathnapura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.052 |  |
| 2026-05-29 23:10:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:06:12 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.048 |  |
| 2026-05-29 23:05:57 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | -0.020 |  |
| 2026-05-29 23:05:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:04:40 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-05-29 23:04:17 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.031 |  |
| 2026-05-29 23:04:17 | Baddegama (Gin Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-29 23:04:09 | Magura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.049 |  |
| 2026-05-29 23:04:00 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-29 23:03:51 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:43 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.012 |  |
| 2026-05-29 23:03:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:39 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:18 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-29 23:03:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:02:52 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.012 |  |
| 2026-05-29 23:02:23 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-29 23:02:19 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:02:16 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-05-29 23:02:15 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-05-29 23:02:11 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-05-29 23:02:08 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:02:08 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.021 |  |
| 2026-05-29 23:02:07 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:01:54 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.023 |  |
| 2026-05-29 23:01:45 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:01:39 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-05-29 23:01:38 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.054 |  |
| 2026-05-29 23:01:30 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.062 |  |
| 2026-05-29 23:01:11 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | -0.019 |  |
| 2026-05-29 23:00:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 23:00:20 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-05-29 23:01:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 6.65 | 🟠 Minor Flood | -0.019 |  |
| 2026-05-29 23:04:00 | Peradeniya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.153 | 🔺 Rising |
| 2026-05-29 23:03:17 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-05-29 23:00:49 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-05-29 23:02:19 | Wellawaya (Kirindi Oya) | 0.95 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:18 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-05-29 22:00:57 | Moragaswewa (Deduru Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:02:08 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:04:21 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:39 | Norwood (Kelani Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:10:50 | Padiyathalawa (Maduru Oya) | 0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:01:11 | Moraketiya (Walawe Ganga) | 0.92 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:39 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:00:20 | Thaldena (Mahaweli Ganga) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:05:55 | Katharagama (Menik Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:51 | Holombuwa (Kelani Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:03:12 | Manampitiya (Mahaweli Ganga) | -0.10 | 🟢 Normal | 0.000 |  |
| 2026-05-29 18:01:26 | Thanthirimale (Malwathu Oya) | 1.18 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:02:07 | Kuda Oya (Kirindi Oya) | 1.34 | 🟢 Normal | 0.000 |  |
| 2026-05-29 23:04:17 | Baddegama (Gin Ganga) | 3.24 | 🟢 Normal | -0.010 |  |
| 2026-05-29 23:01:39 | Thawalama (Gin Ganga) | 2.15 | 🟢 Normal | -0.011 |  |
| 2026-05-29 23:03:43 | Putupaula (Kalu Ganga) | 2.67 | 🟢 Normal | -0.012 |  |
| 2026-05-29 23:02:52 | Giriulla (Maha Oya) | 1.20 | 🟢 Normal | -0.012 |  |
| 2026-05-29 23:02:23 | Deraniyagala (Kelani Ganga) | 1.38 | 🟢 Normal | -0.020 |  |
| 2026-05-29 23:05:57 | Ellagawa (Kalu Ganga) | 8.40 | 🟢 Normal | -0.020 |  |
| 2026-05-29 23:02:08 | Glencourse (Kelani Ganga) | 10.98 | 🟢 Normal | -0.021 |  |
| 2026-05-29 23:02:11 | Urawa (Nilwala Ganga) | 0.45 | 🟢 Normal | -0.021 |  |
| 2026-05-29 23:04:40 | Thanamalwila (Kirindi Oya) | 0.71 | 🟢 Normal | -0.021 |  |
| 2026-05-29 23:01:54 | Panadugama (Nilwala Ganga) | 4.37 | 🟢 Normal | -0.023 |  |
| 2026-05-29 23:04:17 | Badalgama (Maha Oya) | 2.51 | 🟢 Normal | -0.031 |  |
| 2026-05-29 18:00:31 | Weraganthota (Mahaweli Ganga) | -3.28 | 🟢 Normal | -0.034 |  |
| 2026-05-29 23:02:16 | Thalgahagoda (Nilwala Ganga) | 0.89 | 🟢 Normal | -0.040 |  |
| 2026-05-29 23:06:12 | Pitabeddara (Nilwala Ganga) | 1.05 | 🟢 Normal | -0.048 |  |
| 2026-05-29 23:04:09 | Magura (Kalu Ganga) | 3.83 | 🟢 Normal | -0.049 |  |
| 2026-05-29 23:24:01 | Rathnapura (Kalu Ganga) | 3.61 | 🟢 Normal | -0.052 |  |
| 2026-05-29 23:01:38 | Dunamale (Aththanagalu Oya) | 1.93 | 🟢 Normal | -0.054 |  |
| 2026-05-29 23:02:15 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | -0.061 |  |
| 2026-05-29 23:01:30 | Hanwella (Kelani Ganga) | 3.34 | 🟢 Normal | -0.062 |  |
| 2026-05-29 22:03:49 | Nawalapitiya (Mahaweli Ganga) | 1.72 | 🟢 Normal | -0.069 |  |

## River Water Level Charts by Station

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)