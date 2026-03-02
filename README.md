# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--02_21:33:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **87,494 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 21:33:30 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:33:12 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:10:10 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-03-02 21:09:54 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-03-02 21:09:30 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:08:14 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.081 |  |
| 2026-03-02 21:08:10 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-02 21:07:03 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-03-02 21:06:41 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:42 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:39 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:36 | Rathnapura (Kalu Ganga) | 0.53 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-03-02 21:04:34 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:25 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:03 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:03:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:03:33 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:03:31 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:03:18 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-02 21:03:10 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.058 |  |
| 2026-03-02 21:03:09 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-02 21:02:54 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:02:52 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-03-02 21:02:50 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 21:02:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:02:22 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-02 21:02:16 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:02:15 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:02:14 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-03-02 21:01:25 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.223 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-02 21:07:03 | Rathnapura (Kalu Ganga) | 0.54 | 🟢 Normal | 0.245 | 🔺 Rising |
| 2026-03-02 21:01:25 | Peradeniya (Mahaweli Ganga) | 1.35 | 🟢 Normal | 0.223 | 🔺 Rising |
| 2026-03-02 18:07:20 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.162 | 🔺 Rising |
| 2026-03-02 21:02:22 | Dunamale (Aththanagalu Oya) | 1.35 | 🟢 Normal | 0.090 | 🔺 Rising |
| 2026-03-02 21:08:10 | Nagalagam Street (Kelani Ganga) | 0.24 | 🟢 Normal | 0.086 | 🔺 Rising |
| 2026-03-02 20:04:10 | Thawalama (Gin Ganga) | 1.12 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-02 21:02:50 | Deraniyagala (Kelani Ganga) | 0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-02 21:02:54 | Kithulgala (Kelani Ganga) | 1.78 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:00:39 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:03 | Nakkala (Kumbukkan Oya) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:02:26 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:00:29 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:00:48 | Yaka Wewa (Ma Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:03:31 | Giriulla (Maha Oya) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-02 18:00:46 | Galgamuwa (Mee Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:02:16 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:09:30 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:33:30 | Panadugama (Nilwala Ganga) | 1.96 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:39 | Glencourse (Kelani Ganga) | 8.26 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:34 | Moraketiya (Walawe Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:00:24 | Siyambalanduwa (Heda Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:03:40 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:42 | Badalgama (Maha Oya) | 1.76 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:06:41 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:04:25 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:02:15 | Kuda Oya (Kirindi Oya) | 1.13 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:03:33 | Thanamalwila (Kirindi Oya) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:09:04 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.37 | 🟢 Normal | 0.000 |  |
| 2026-03-02 21:10:10 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | -0.009 |  |
| 2026-03-02 21:09:54 | Pitabeddara (Nilwala Ganga) | 0.20 | 🟢 Normal | -0.009 |  |
| 2026-03-02 18:03:36 | Thanthirimale (Malwathu Oya) | 0.86 | 🟢 Normal | -0.010 |  |
| 2026-03-02 21:03:18 | Ellagawa (Kalu Ganga) | 3.88 | 🟢 Normal | -0.010 |  |
| 2026-03-02 21:02:14 | Manampitiya (Mahaweli Ganga) | 1.35 | 🟢 Normal | -0.010 |  |
| 2026-03-02 20:04:40 | Horowpothana (Yan Oya) | 1.14 | 🟢 Normal | -0.017 |  |
| 2026-03-02 21:03:09 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | -0.019 |  |
| 2026-03-02 21:02:52 | Hanwella (Kelani Ganga) | 0.20 | 🟢 Normal | -0.030 |  |
| 2026-03-02 21:03:10 | Thalgahagoda (Nilwala Ganga) | 0.23 | 🟢 Normal | -0.058 |  |
| 2026-03-02 21:08:14 | Putupaula (Kalu Ganga) | 0.27 | 🟢 Normal | -0.081 |  |
| 2026-03-02 20:10:32 | Magura (Kalu Ganga) | 0.73 | 🟢 Normal | -36.000 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)