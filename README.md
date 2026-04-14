# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--14_06:29:32-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **124,589 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 06:29:32 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-04-14 06:11:01 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.054 |  |
| 2026-04-14 06:10:06 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:08:58 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:08:57 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-04-14 06:08:56 | Thanamalwila (Kirindi Oya) | 1.52 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-04-14 06:08:25 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-04-14 06:07:13 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-14 06:06:58 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 06:06:16 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:05:36 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-14 06:05:20 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:04:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:04:38 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-04-14 06:04:35 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-04-14 06:04:17 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.057 |  |
| 2026-04-14 06:03:58 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:03:42 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.053 |  |
| 2026-04-14 06:03:24 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 06:03:21 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.635 |  |
| 2026-04-14 06:03:21 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:03:10 | Kuda Oya (Kirindi Oya) | 1.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-14 06:03:00 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 06:02:58 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-14 06:02:40 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-04-14 06:02:11 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.154 |  |
| 2026-04-14 06:02:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |
| 2026-04-14 06:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -1.835 |  |
| 2026-04-14 06:02:03 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.051 |  |
| 2026-04-14 06:01:41 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.080 |  |
| 2026-04-14 06:01:28 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-14 06:01:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:01:12 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-14 06:01:10 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.208 |  |
| 2026-04-14 06:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.079 |  |
| 2026-04-14 06:00:52 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 06:00:45 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-14 06:00:34 | Manampitiya (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-04-14 06:00:23 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 06:00:13 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 05:53:37 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.17 | 🟢 Normal | -1.835 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-14 06:08:57 | Thanamalwila (Kirindi Oya) | 1.66 | 🟢 Normal | 504.000 | 🔺 Rising |
| 2026-04-14 06:04:38 | Manampitiya (Mahaweli Ganga) | 0.19 | 🟢 Normal | 0.295 | 🔺 Rising |
| 2026-04-14 06:02:58 | Deraniyagala (Kelani Ganga) | 0.33 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-04-14 06:00:52 | Nakkala (Kumbukkan Oya) | 0.84 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-04-14 06:00:45 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-04-14 06:00:23 | Rathnapura (Kalu Ganga) | 1.26 | 🟢 Normal | 0.052 | 🔺 Rising |
| 2026-04-14 06:03:10 | Kuda Oya (Kirindi Oya) | 1.96 | 🟢 Normal | 0.039 | 🔺 Rising |
| 2026-04-14 06:01:28 | Weraganthota (Mahaweli Ganga) | -2.75 | 🟢 Normal | 0.023 | 🔺 Rising |
| 2026-04-14 06:03:00 | Siyambalanduwa (Heda Oya) | 0.55 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 06:03:24 | Moragaswewa (Deduru Oya) | 0.78 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-14 06:01:12 | Norwood (Kelani Ganga) | 0.70 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-13 18:01:02 | Thanthirimale (Malwathu Oya) | 1.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 06:06:58 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-14 06:01:16 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:00:13 | Wellawaya (Kirindi Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:05:20 | Yaka Wewa (Ma Oya) | 0.56 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:03:21 | Giriulla (Maha Oya) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:10:06 | Horowpothana (Yan Oya) | 1.53 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:06:16 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:08:58 | Panadugama (Nilwala Ganga) | 2.03 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:04:54 | Padiyathalawa (Maduru Oya) | 0.24 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:03:58 | Dunamale (Aththanagalu Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-04-14 06:07:13 | Urawa (Nilwala Ganga) | 0.07 | 🟢 Normal | -0.010 |  |
| 2026-04-14 06:02:40 | Thawalama (Gin Ganga) | 1.39 | 🟢 Normal | -0.011 |  |
| 2026-04-14 06:29:32 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | -0.011 |  |
| 2026-04-14 06:08:25 | Holombuwa (Kelani Ganga) | 0.28 | 🟢 Normal | -0.012 |  |
| 2026-04-14 06:05:36 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | -0.019 |  |
| 2026-04-14 06:04:35 | Badalgama (Maha Oya) | 2.10 | 🟢 Normal | -0.019 |  |
| 2026-04-14 06:02:03 | Glencourse (Kelani Ganga) | 8.70 | 🟢 Normal | -0.051 |  |
| 2026-04-14 06:03:42 | Thaldena (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.053 |  |
| 2026-04-14 06:11:01 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.054 |  |
| 2026-04-14 06:04:17 | Ellagawa (Kalu Ganga) | 4.79 | 🟢 Normal | -0.057 |  |
| 2026-04-14 06:02:08 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.061 |  |
| 2026-04-14 06:00:59 | Nawalapitiya (Mahaweli Ganga) | 0.83 | 🟢 Normal | -0.079 |  |
| 2026-04-14 06:01:41 | Magura (Kalu Ganga) | 1.65 | 🟢 Normal | -0.080 |  |
| 2026-04-14 06:02:11 | Peradeniya (Mahaweli Ganga) | 1.36 | 🟢 Normal | -0.154 |  |
| 2026-04-14 06:01:10 | Putupaula (Kalu Ganga) | 0.47 | 🟢 Normal | -0.208 |  |
| 2026-04-14 06:03:21 | Katharagama (Menik Ganga) | 0.17 | 🟢 Normal | -0.635 |  |
| 2026-04-14 06:02:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.91 | 🟢 Normal | -1.835 |  |

## River Water Level Charts by Station

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)