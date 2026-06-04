# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--04_17:16:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **170,403 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **6** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 17:16:16 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:12:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.005 |  |
| 2026-06-04 17:12:11 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:11:12 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:11:05 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-04 17:10:18 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.009 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-04 17:02:49 | Kithulgala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.104 | 🔺 Rising |
| 2026-06-04 17:02:20 | Deraniyagala (Kelani Ganga) | 1.82 | 🟢 Normal | 0.094 | 🔺 Rising |
| 2026-06-04 17:03:29 | Glencourse (Kelani Ganga) | 10.97 | 🟢 Normal | 0.072 | 🔺 Rising |
| 2026-06-04 17:01:58 | Nawalapitiya (Mahaweli Ganga) | 2.09 | 🟢 Normal | 0.068 | 🔺 Rising |
| 2026-06-04 17:02:20 | Thalgahagoda (Nilwala Ganga) | 0.56 | 🟢 Normal | 0.061 | 🔺 Rising |
| 2026-06-04 17:04:39 | Holombuwa (Kelani Ganga) | 0.90 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-04 17:04:39 | Rathnapura (Kalu Ganga) | 2.77 | 🟢 Normal | 0.059 | 🔺 Rising |
| 2026-06-04 17:02:18 | Dunamale (Aththanagalu Oya) | 1.48 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-06-04 17:03:52 | Hanwella (Kelani Ganga) | 2.60 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-06-04 17:04:01 | Putupaula (Kalu Ganga) | 0.91 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 17:02:49 | Moragaswewa (Deduru Oya) | 0.38 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-06-04 17:03:38 | Ellagawa (Kalu Ganga) | 6.42 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-06-04 17:11:05 | Peradeniya (Mahaweli Ganga) | 2.12 | 🟢 Normal | 0.018 | 🔺 Rising |
| 2026-06-04 17:06:12 | Badalgama (Maha Oya) | 2.19 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 17:02:45 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-04 17:10:18 | Weraganthota (Mahaweli Ganga) | -3.31 | 🟢 Normal | 0.009 | 🔺 Rising |
| 2026-06-04 17:00:15 | Nakkala (Kumbukkan Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:00:34 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:09:00 | Giriulla (Maha Oya) | 1.11 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:01:22 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:12:11 | Galgamuwa (Mee Oya) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:11:12 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:01:40 | Baddegama (Gin Ganga) | 1.86 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:16:16 | Panadugama (Nilwala Ganga) | 2.89 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:06:17 | Padiyathalawa (Maduru Oya) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:02:28 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:00:18 | Siyambalanduwa (Heda Oya) | 0.39 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:07:34 | Manampitiya (Mahaweli Ganga) | -0.18 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:01:05 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:02:33 | Thanamalwila (Kirindi Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-04 17:12:31 | Pitabeddara (Nilwala Ganga) | 0.85 | 🟢 Normal | -0.005 |  |
| 2026-06-04 17:03:22 | Kuda Oya (Kirindi Oya) | 1.21 | 🟢 Normal | -0.005 |  |
| 2026-06-04 17:00:15 | Wellawaya (Kirindi Oya) | 0.68 | 🟢 Normal | -0.010 |  |
| 2026-06-04 17:01:37 | Thaldena (Mahaweli Ganga) | 0.23 | 🟢 Normal | -0.010 |  |
| 2026-06-04 17:03:56 | Urawa (Nilwala Ganga) | 0.37 | 🟢 Normal | -0.012 |  |
| 2026-06-04 17:02:56 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.08 | 🟢 Normal | -0.027 |  |
| 2026-06-04 17:04:22 | Thawalama (Gin Ganga) | 1.82 | 🟢 Normal | -0.030 |  |
| 2026-06-04 17:09:00 | Norwood (Kelani Ganga) | 0.72 | 🟢 Normal | -0.054 |  |
| 2026-06-04 17:05:59 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | -0.059 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)