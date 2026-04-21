# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--21_06:29:06-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **130,815 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **43** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 06:29:06 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 06:20:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-21 06:14:20 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.026 |  |
| 2026-04-21 06:09:48 | Thanamalwila (Kirindi Oya) | 2.90 | 🟢 Normal | -0.357 |  |
| 2026-04-21 06:08:53 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-21 06:06:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:06:29 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:06:27 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.086 |  |
| 2026-04-21 06:05:51 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 06:05:50 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:05:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.059 |  |
| 2026-04-21 06:05:36 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:05:25 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-21 06:05:07 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -252.000 |  |
| 2026-04-21 06:05:06 | Thaldena (Mahaweli Ganga) | 0.87 | 🟢 Normal | -252.000 |  |
| 2026-04-21 06:04:46 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-21 06:04:43 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.149 |  |
| 2026-04-21 06:04:26 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.123 |  |
| 2026-04-21 06:04:20 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-21 06:04:17 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-21 06:04:17 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:04:06 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:03:43 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-21 06:03:36 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:03:31 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-04-21 06:03:30 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 06:03:23 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-21 06:02:33 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:02:33 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.657 | 🔺 Rising |
| 2026-04-21 06:02:14 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-04-21 06:02:06 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.077 |  |
| 2026-04-21 06:01:29 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-21 06:01:28 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-21 06:01:27 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-21 06:01:26 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-04-21 06:01:12 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.770 |  |
| 2026-04-21 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.408 |  |
| 2026-04-21 06:00:59 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.042 |  |
| 2026-04-21 06:00:33 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.085 |  |
| 2026-04-21 06:00:24 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-21 05:59:47 | Thalgahagoda (Nilwala Ganga) | 0.44 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-21 05:50:53 | Panadugama (Nilwala Ganga) | 2.70 | 🟢 Normal | -0.026 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-21 06:02:33 | Giriulla (Maha Oya) | 1.88 | 🟢 Normal | 0.657 | 🔺 Rising |
| 2026-04-21 06:02:14 | Hanwella (Kelani Ganga) | 1.86 | 🟢 Normal | 0.432 | 🔺 Rising |
| 2026-04-21 06:03:23 | Deraniyagala (Kelani Ganga) | 0.42 | 🟢 Normal | 0.288 | 🔺 Rising |
| 2026-04-21 06:01:26 | Ellagawa (Kalu Ganga) | 5.83 | 🟢 Normal | 0.184 | 🔺 Rising |
| 2026-04-21 06:20:53 | Thalgahagoda (Nilwala Ganga) | 0.50 | 🟢 Normal | 0.171 | 🔺 Rising |
| 2026-04-21 06:04:46 | Magura (Kalu Ganga) | 1.93 | 🟢 Normal | 0.102 | 🔺 Rising |
| 2026-04-21 06:29:06 | Galgamuwa (Mee Oya) | 1.16 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-04-21 06:04:17 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-04-21 06:01:28 | Putupaula (Kalu Ganga) | 0.86 | 🟢 Normal | 0.064 | 🔺 Rising |
| 2026-04-21 06:03:43 | Urawa (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-04-21 06:01:29 | Wellawaya (Kirindi Oya) | 1.10 | 🟢 Normal | 0.051 | 🔺 Rising |
| 2026-04-21 06:00:09 | Nawalapitiya (Mahaweli Ganga) | 1.08 | 🟢 Normal | 0.044 | 🔺 Rising |
| 2026-04-21 06:08:53 | Baddegama (Gin Ganga) | 1.38 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-21 06:01:27 | Weraganthota (Mahaweli Ganga) | -2.77 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-04-21 06:04:20 | Pitabeddara (Nilwala Ganga) | 0.80 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-04-21 06:05:51 | Katharagama (Menik Ganga) | 0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 06:03:30 | Dunamale (Aththanagalu Oya) | 0.99 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-04-21 06:04:17 | Moragaswewa (Deduru Oya) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:04:06 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:00:24 | Horowpothana (Yan Oya) | 1.41 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:03:36 | Padiyathalawa (Maduru Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:06:41 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:06:29 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:02:33 | Manampitiya (Mahaweli Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-04-21 06:05:25 | Norwood (Kelani Ganga) | 0.74 | 🟢 Normal | -0.010 |  |
| 2026-04-20 18:01:44 | Thanthirimale (Malwathu Oya) | 1.25 | 🟢 Normal | -0.010 |  |
| 2026-04-21 06:14:20 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | -0.026 |  |
| 2026-04-21 06:00:59 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.042 |  |
| 2026-04-21 06:05:44 | Nagalagam Street (Kelani Ganga) | 0.61 | 🟢 Normal | -0.059 |  |
| 2026-04-21 06:03:31 | Kithulgala (Kelani Ganga) | 1.45 | 🟢 Normal | -0.060 |  |
| 2026-04-21 06:02:06 | Moraketiya (Walawe Ganga) | 1.13 | 🟢 Normal | -0.077 |  |
| 2026-04-21 06:00:33 | Rathnapura (Kalu Ganga) | 3.10 | 🟢 Normal | -0.085 |  |
| 2026-04-21 06:06:27 | Holombuwa (Kelani Ganga) | 0.70 | 🟢 Normal | -0.086 |  |
| 2026-04-21 06:04:26 | Glencourse (Kelani Ganga) | 10.44 | 🟢 Normal | -0.123 |  |
| 2026-04-21 06:04:43 | Peradeniya (Mahaweli Ganga) | 1.89 | 🟢 Normal | -0.149 |  |
| 2026-04-21 06:09:48 | Thanamalwila (Kirindi Oya) | 2.90 | 🟢 Normal | -0.357 |  |
| 2026-04-21 06:01:07 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.64 | 🟢 Normal | -0.408 |  |
| 2026-04-21 06:01:12 | Kuda Oya (Kirindi Oya) | 2.07 | 🟢 Normal | -0.770 |  |
| 2026-04-21 06:05:07 | Thaldena (Mahaweli Ganga) | 0.80 | 🟢 Normal | -252.000 |  |

## River Water Level Charts by Station

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)