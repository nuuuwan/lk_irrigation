# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--06_06:11:53-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,470 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **38** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 06:11:53 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:10:43 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-04-06 06:10:05 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-06 06:07:18 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:06:59 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:06:16 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:06:14 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 06:06:09 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:06:03 | Hanwella (Kelani Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-04-06 06:05:46 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-06 06:05:31 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:05:28 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.028 |  |
| 2026-04-06 06:04:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.104 |  |
| 2026-04-06 06:04:30 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 06:04:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-04-06 06:04:14 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-06 06:03:47 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-06 06:03:38 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.070 |  |
| 2026-04-06 06:02:57 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:49 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-06 06:02:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:45 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:34 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:32 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:19 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-04-06 06:01:56 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-06 06:01:50 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:01:42 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-06 06:01:39 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.080 |  |
| 2026-04-06 06:01:38 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:01:32 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.047 |  |
| 2026-04-06 06:01:13 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-04-06 06:01:12 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:01:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-06 06:00:24 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-06 06:00:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-06 06:01:13 | Glencourse (Kelani Ganga) | 8.69 | 🟢 Normal | 0.188 | 🔺 Rising |
| 2026-04-06 06:01:42 | Weraganthota (Mahaweli Ganga) | -2.14 | 🟢 Normal | 0.081 | 🔺 Rising |
| 2026-04-06 06:01:56 | Thalgahagoda (Nilwala Ganga) | 0.53 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-04-06 06:03:47 | Deraniyagala (Kelani Ganga) | 0.25 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-04-06 06:00:24 | Rathnapura (Kalu Ganga) | 0.62 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-06 06:04:30 | Badalgama (Maha Oya) | 1.84 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-06 06:06:14 | Thaldena (Mahaweli Ganga) | 0.25 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-04-06 06:01:38 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:57 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:32 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:01:32 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:01:12 | Magura (Kalu Ganga) | 0.72 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:47 | Pitabeddara (Nilwala Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:06:59 | Norwood (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:06:09 | Baddegama (Gin Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:06:16 | Padiyathalawa (Maduru Oya) | 0.28 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:00:23 | Moraketiya (Walawe Ganga) | 0.98 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:34 | Siyambalanduwa (Heda Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:02:23 | Dunamale (Aththanagalu Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:07:18 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:11:53 | Thawalama (Gin Ganga) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:01:50 | Kuda Oya (Kirindi Oya) | 1.15 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:05:31 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-04-06 06:10:05 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | -0.009 |  |
| 2026-04-06 06:04:14 | Urawa (Nilwala Ganga) | -0.02 | 🟢 Normal | -0.010 |  |
| 2026-04-06 06:02:49 | Giriulla (Maha Oya) | 0.79 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-06 06:01:09 | Kithulgala (Kelani Ganga) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-04-06 06:02:19 | Panadugama (Nilwala Ganga) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-04-06 06:05:46 | Nawalapitiya (Mahaweli Ganga) | 0.49 | 🟢 Normal | -0.020 |  |
| 2026-04-06 06:05:28 | Ellagawa (Kalu Ganga) | 4.04 | 🟢 Normal | -0.028 |  |
| 2026-04-06 06:10:43 | Horowpothana (Yan Oya) | 1.51 | 🟢 Normal | -0.039 |  |
| 2026-04-06 06:06:03 | Hanwella (Kelani Ganga) | 0.21 | 🟢 Normal | -0.041 |  |
| 2026-04-06 06:01:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.76 | 🟢 Normal | -0.047 |  |
| 2026-04-06 06:04:18 | Putupaula (Kalu Ganga) | 0.70 | 🟢 Normal | -0.063 |  |
| 2026-04-06 06:03:38 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.070 |  |
| 2026-04-06 06:01:39 | Manampitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | -0.080 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-06 06:04:58 | Nagalagam Street (Kelani Ganga) | 0.49 | 🟢 Normal | -0.104 |  |

## River Water Level Charts by Station

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)