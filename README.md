# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--16_18:14:19-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **99,134 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **40** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 18:14:19 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:13:39 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:11:17 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:11:13 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:08:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:08:49 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-16 18:07:42 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:07:25 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.174 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:19 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-16 18:03:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 18:03:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-03-16 18:03:30 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.029 |  |
| 2026-03-16 18:03:28 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:27 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 18:03:19 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:10 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:04 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-03-16 18:03:00 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:02:38 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-16 18:02:31 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:02:30 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:02:29 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-16 18:02:09 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-03-16 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-03-16 18:02:06 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:02:05 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.102 |  |
| 2026-03-16 18:02:01 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:59 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-03-16 18:01:33 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:01:19 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-03-16 18:01:06 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:00:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:00:18 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |
| 2026-03-16 18:00:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.053 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-16 18:03:40 | Kithulgala (Kelani Ganga) | 1.73 | 🟢 Normal | 0.322 | 🔺 Rising |
| 2026-03-16 18:02:29 | Deraniyagala (Kelani Ganga) | 0.30 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-16 18:00:06 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-16 18:02:38 | Baddegama (Gin Ganga) | 0.91 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-03-16 18:04:19 | Rathnapura (Kalu Ganga) | 0.43 | 🟢 Normal | 0.013 | 🔺 Rising |
| 2026-03-16 18:03:27 | Holombuwa (Kelani Ganga) | 0.26 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 18:03:47 | Moraketiya (Walawe Ganga) | 0.65 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-16 18:08:49 | Manampitiya (Mahaweli Ganga) | 0.78 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-16 18:02:06 | Nakkala (Kumbukkan Oya) | 0.78 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:01 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:10 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:02:30 | Giriulla (Maha Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:14:19 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:04:59 | Galgamuwa (Mee Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:13:39 | Magura (Kalu Ganga) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:11:17 | Pitabeddara (Nilwala Ganga) | 0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:19 | Hanwella (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:11:13 | Padiyathalawa (Maduru Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:02:01 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:04 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:58 | Thanthirimale (Malwathu Oya) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:03:28 | Thawalama (Gin Ganga) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:08:49 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:06 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:02:31 | Thanamalwila (Kirindi Oya) | 0.90 | 🟢 Normal | 0.000 |  |
| 2026-03-16 18:01:59 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:00:18 | Wellawaya (Kirindi Oya) | 0.89 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:07:42 | Panadugama (Nilwala Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:01:33 | Norwood (Kelani Ganga) | 0.39 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:00:22 | Thaldena (Mahaweli Ganga) | 0.46 | 🟢 Normal | -0.010 |  |
| 2026-03-16 18:02:09 | Badalgama (Maha Oya) | 1.91 | 🟢 Normal | -0.011 |  |
| 2026-03-16 18:03:02 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | -0.011 |  |
| 2026-03-16 18:02:09 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.39 | 🟢 Normal | -0.020 |  |
| 2026-03-16 18:01:19 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | -0.021 |  |
| 2026-03-16 18:01:37 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.022 |  |
| 2026-03-16 18:03:30 | Glencourse (Kelani Ganga) | 8.48 | 🟢 Normal | -0.029 |  |
| 2026-03-16 18:02:05 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.102 |  |
| 2026-03-16 18:07:25 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | -0.174 |  |
| 2026-03-16 18:00:13 | Weraganthota (Mahaweli Ganga) | -2.95 | 🟢 Normal | -0.210 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)