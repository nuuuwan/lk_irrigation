# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_19:01:55-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **97,351 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 19:01:55 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:01:44 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:30 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:01:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:11 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:00:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:00:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:14:12 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.014 |  |
| 2026-03-14 18:12:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-14 18:12:18 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:08:31 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 18:02:24 | Dunamale (Aththanagalu Oya) | 0.98 | 🟢 Normal | 0.138 | 🔺 Rising |
| 2026-03-14 18:04:19 | Badalgama (Maha Oya) | 1.98 | 🟢 Normal | 0.053 | 🔺 Rising |
| 2026-03-14 18:12:23 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-03-14 18:02:22 | Thanamalwila (Kirindi Oya) | 0.65 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 18:01:43 | Glencourse (Kelani Ganga) | 8.65 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 18:06:24 | Norwood (Kelani Ganga) | 0.49 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-03-14 19:00:17 | Wellawaya (Kirindi Oya) | 0.93 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:00:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:02:00 | Moragaswewa (Deduru Oya) | 0.21 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:44 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:12:18 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:23 | Galgamuwa (Mee Oya) | 0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:21 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:20 | Baddegama (Gin Ganga) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:30 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:16 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:10 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:02:45 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:12 | Katharagama (Menik Ganga) | -0.24 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:01:03 | Thanthirimale (Malwathu Oya) | 1.10 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:03:08 | Thawalama (Gin Ganga) | 1.20 | 🟢 Normal | 0.000 |  |
| 2026-03-14 18:06:23 | Urawa (Nilwala Ganga) | 0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-14 19:01:11 | Kuda Oya (Kirindi Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-14 17:10:52 | Giriulla (Maha Oya) | 0.95 | 🟢 Normal | -0.009 |  |
| 2026-03-14 18:02:44 | Pitabeddara (Nilwala Ganga) | 0.30 | 🟢 Normal | -0.010 |  |
| 2026-03-14 18:01:40 | Magura (Kalu Ganga) | 0.75 | 🟢 Normal | -0.011 |  |
| 2026-03-14 18:01:19 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | -0.013 |  |
| 2026-03-14 18:14:12 | Rathnapura (Kalu Ganga) | 0.90 | 🟢 Normal | -0.014 |  |
| 2026-03-14 18:05:58 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.77 | 🟢 Normal | -0.019 |  |
| 2026-03-14 19:01:55 | Manampitiya (Mahaweli Ganga) | 0.93 | 🟢 Normal | -0.020 |  |
| 2026-03-14 18:04:14 | Panadugama (Nilwala Ganga) | 2.16 | 🟢 Normal | -0.020 |  |
| 2026-03-14 19:01:26 | Nawalapitiya (Mahaweli Ganga) | 0.76 | 🟢 Normal | -0.020 |  |
| 2026-03-14 18:03:13 | Hanwella (Kelani Ganga) | 0.69 | 🟢 Normal | -0.040 |  |
| 2026-03-14 18:01:41 | Putupaula (Kalu Ganga) | 0.50 | 🟢 Normal | -0.041 |  |
| 2026-03-14 18:03:08 | Deraniyagala (Kelani Ganga) | 0.23 | 🟢 Normal | -0.050 |  |
| 2026-03-14 18:00:54 | Thaldena (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.070 |  |
| 2026-03-14 18:05:56 | Kithulgala (Kelani Ganga) | 1.36 | 🟢 Normal | -0.087 |  |
| 2026-03-14 18:02:56 | Thalgahagoda (Nilwala Ganga) | 0.41 | 🟢 Normal | -0.095 |  |
| 2026-03-14 18:01:50 | Weraganthota (Mahaweli Ganga) | -2.87 | 🟢 Normal | -0.100 |  |

## River Water Level Charts by Station

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)