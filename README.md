# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--20_20:34:29-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **102,786 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **18** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 20:34:29 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:19:49 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:13:00 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:11:46 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:10:29 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.034 |  |
| 2026-03-20 20:09:08 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-03-20 20:08:42 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.027 |  |
| 2026-03-20 20:08:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:08:17 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.083 |  |
| 2026-03-20 20:07:05 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:06:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.149 |  |
| 2026-03-20 20:06:38 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.216 |  |
| 2026-03-20 20:06:36 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-20 20:05:30 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:05:30 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-03-20 20:05:09 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:05:01 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:04:42 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-20 20:06:36 | Baddegama (Gin Ganga) | 1.21 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-20 20:00:11 | Wellawaya (Kirindi Oya) | 0.74 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-03-20 20:02:27 | Kithulgala (Kelani Ganga) | 1.93 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-20 20:01:30 | Dunamale (Aththanagalu Oya) | 0.48 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-20 18:01:37 | Thanthirimale (Malwathu Oya) | 1.39 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-20 20:01:18 | Nakkala (Kumbukkan Oya) | 0.77 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:34:29 | Moragaswewa (Deduru Oya) | 0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:00:49 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:02:43 | Yaka Wewa (Ma Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:05:30 | Horowpothana (Yan Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 18:02:58 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:19:49 | Pitabeddara (Nilwala Ganga) | 0.35 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:03:03 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:02:32 | Hanwella (Kelani Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:07:05 | Padiyathalawa (Maduru Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:00:44 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:05:01 | Katharagama (Menik Ganga) | -0.19 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:05:09 | Badalgama (Maha Oya) | 1.95 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:00:56 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:01:33 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:02:46 | Peradeniya (Mahaweli Ganga) | 1.02 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:11:46 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:13:00 | Thalgahagoda (Nilwala Ganga) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:08:20 | Kuda Oya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:02:15 | Thanamalwila (Kirindi Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-20 20:02:08 | Siyambalanduwa (Heda Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-03-20 20:02:22 | Thaldena (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-03-20 20:04:09 | Giriulla (Maha Oya) | 0.85 | 🟢 Normal | -0.011 |  |
| 2026-03-20 20:04:42 | Deraniyagala (Kelani Ganga) | 0.11 | 🟢 Normal | -0.019 |  |
| 2026-03-20 20:09:08 | Thawalama (Gin Ganga) | 1.42 | 🟢 Normal | -0.022 |  |
| 2026-03-20 20:08:42 | Magura (Kalu Ganga) | 0.87 | 🟢 Normal | -0.027 |  |
| 2026-03-20 20:10:29 | Panadugama (Nilwala Ganga) | 2.17 | 🟢 Normal | -0.034 |  |
| 2026-03-20 20:05:30 | Rathnapura (Kalu Ganga) | 0.77 | 🟢 Normal | -0.040 |  |
| 2026-03-20 20:08:17 | Glencourse (Kelani Ganga) | 8.40 | 🟢 Normal | -0.083 |  |
| 2026-03-20 18:01:16 | Weraganthota (Mahaweli Ganga) | -2.88 | 🟢 Normal | -0.091 |  |
| 2026-03-20 20:06:51 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.80 | 🟢 Normal | -0.149 |  |
| 2026-03-20 20:03:09 | Nagalagam Street (Kelani Ganga) | 0.21 | 🟢 Normal | -0.184 |  |
| 2026-03-20 20:06:38 | Ellagawa (Kalu Ganga) | 4.00 | 🟢 Normal | -0.216 |  |
| 2026-03-20 20:02:09 | Putupaula (Kalu Ganga) | 0.60 | 🟢 Normal | -0.346 |  |

## River Water Level Charts by Station

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)