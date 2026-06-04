# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_19:04:52-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,466 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 19:04:52 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:04:23 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-04 19:04:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-04 19:03:51 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:39 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:37 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:20 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:18 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-06-04 19:03:11 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:02:53 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 19:02:49 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 19:02:47 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-04 19:02:41 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-04 19:02:37 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 19:02:36 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:02:35 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 19:02:17 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 19:02:12 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:01:55 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-04 19:01:21 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:01:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:01:10 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | 0.187 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 18:02:00 | Kithulgala (Kelani Ganga) | 2.05 | 🟢 Normal | 0.233 | 🔺 Rising |
| 2026-06-04 19:01:10 | Peradeniya (Mahaweli Ganga) | 2.33 | 🟢 Normal | 0.187 | 🔺 Rising |
| 2026-06-04 19:03:18 | Glencourse (Kelani Ganga) | 11.26 | 🟢 Normal | 0.160 | 🔺 Rising |
| 2026-06-04 19:04:23 | Rathnapura (Kalu Ganga) | 2.95 | 🟢 Normal | 0.096 | 🔺 Rising |
| 2026-06-04 19:02:47 | Deraniyagala (Kelani Ganga) | 2.15 | 🟢 Normal | 0.080 | 🔺 Rising |
| 2026-06-04 19:01:55 | Holombuwa (Kelani Ganga) | 1.01 | 🟢 Normal | 0.071 | 🔺 Rising |
| 2026-06-04 18:03:30 | Nawalapitiya (Mahaweli Ganga) | 2.15 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-04 19:02:37 | Hanwella (Kelani Ganga) | 2.69 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-06-04 19:02:17 | Dunamale (Aththanagalu Oya) | 1.54 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 19:02:53 | Thaldena (Mahaweli Ganga) | 0.24 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 18:03:10 | Magura (Kalu Ganga) | 2.03 | 🟢 Normal | 0.035 | 🔺 Rising |
| 2026-06-04 18:01:11 | Ellagawa (Kalu Ganga) | 6.45 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 18:05:44 | Giriulla (Maha Oya) | 1.13 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-06-04 18:00:13 | Weraganthota (Mahaweli Ganga) | -3.30 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-06-04 19:02:49 | Badalgama (Maha Oya) | 2.20 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 18:00:16 | Putupaula (Kalu Ganga) | 0.92 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 19:02:35 | Moragaswewa (Deduru Oya) | 0.41 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-04 18:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.09 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 19:03:34 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:04:52 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:08:03 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:01:15 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:07:04 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:11 | Pitabeddara (Nilwala Ganga) | 0.84 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:37 | Baddegama (Gin Ganga) | 1.87 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:51 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:01:11 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:02:12 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:05:03 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:02:36 | Manampitiya (Mahaweli Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:03:20 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:39 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-04 18:00:07 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:01:21 | Kuda Oya (Kirindi Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:03:20 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 19:02:41 | Norwood (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-04 18:06:20 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.012 |  |
| 2026-06-04 19:04:06 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.030 |  |
| 2026-06-04 18:02:50 | Thawalama (Gin Ganga) | 1.79 | 🟢 Normal | -0.031 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

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

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)