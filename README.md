# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--24_07:00:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **105,815 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **11** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 07:00:56 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 07:00:35 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 07:00:19 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-24 06:26:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:11:09 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:10:01 | Weraganthota (Mahaweli Ganga) | -2.48 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-24 06:09:56 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.327 |  |
| 2026-03-24 06:09:52 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:08:46 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.075 |  |
| 2026-03-24 06:07:23 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-03-24 06:06:44 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-24 06:01:37 | Kithulgala (Kelani Ganga) | 1.61 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-03-24 06:04:14 | Glencourse (Kelani Ganga) | 8.49 | 🟢 Normal | 0.091 | 🔺 Rising |
| 2026-03-24 06:02:42 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-24 07:00:19 | Weraganthota (Mahaweli Ganga) | -2.42 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-03-24 06:00:52 | Thalgahagoda (Nilwala Ganga) | 0.39 | 🟢 Normal | 0.058 | 🔺 Rising |
| 2026-03-24 06:05:55 | Holombuwa (Kelani Ganga) | 0.25 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-24 06:02:00 | Moraketiya (Walawe Ganga) | 0.76 | 🟢 Normal | 0.005 |  |
| 2026-03-24 06:01:32 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:02:22 | Nakkala (Kumbukkan Oya) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:00:39 | Moragaswewa (Deduru Oya) | -0.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:01:32 | Nawalapitiya (Mahaweli Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:02:29 | Yaka Wewa (Ma Oya) | 0.58 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:03:03 | Giriulla (Maha Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:03:55 | Horowpothana (Yan Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:26:25 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:04:03 | Magura (Kalu Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-03-24 07:00:35 | Pitabeddara (Nilwala Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:03:01 | Norwood (Kelani Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:02:59 | Ellagawa (Kalu Ganga) | 3.98 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:09:52 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:11:09 | Panadugama (Nilwala Ganga) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:02:09 | Padiyathalawa (Maduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:02:48 | Siyambalanduwa (Heda Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:02:37 | Katharagama (Menik Ganga) | -0.17 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:00:56 | Rathnapura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-24 07:00:56 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:05:27 | Urawa (Nilwala Ganga) | -0.07 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:03:02 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:02:11 | Thanamalwila (Kirindi Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-24 06:03:36 | Thawalama (Gin Ganga) | 1.17 | 🟢 Normal | -0.011 |  |
| 2026-03-24 06:03:00 | Badalgama (Maha Oya) | 1.85 | 🟢 Normal | -0.011 |  |
| 2026-03-24 06:07:23 | Hanwella (Kelani Ganga) | 0.24 | 🟢 Normal | -0.018 |  |
| 2026-03-24 06:04:14 | Manampitiya (Mahaweli Ganga) | 0.48 | 🟢 Normal | -0.019 |  |
| 2026-03-24 06:06:44 | Thaldena (Mahaweli Ganga) | 0.29 | 🟢 Normal | -0.020 |  |
| 2026-03-24 06:05:29 | Peradeniya (Mahaweli Ganga) | 1.15 | 🟢 Normal | -0.046 |  |
| 2026-03-24 06:03:56 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | -0.063 |  |
| 2026-03-24 06:08:46 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | -0.075 |  |
| 2026-03-24 05:53:11 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.84 | 🟢 Normal | -0.162 |  |
| 2026-03-24 06:09:56 | Dunamale (Aththanagalu Oya) | 0.58 | 🟢 Normal | -0.327 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)