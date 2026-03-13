# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--13_12:01:23-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,188 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **14** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 12:01:23 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 12:01:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 12:01:07 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-13 12:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-13 12:00:27 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-13 12:00:07 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-03-13 11:22:04 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:19:43 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:13:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:10:53 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:09:06 | Nawalapitiya (Mahaweli Ganga) | 0.66 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-13 11:08:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-03-13 11:07:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-13 11:06:50 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.011 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-13 11:08:11 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.213 | 🔺 Rising |
| 2026-03-13 12:00:07 | Weraganthota (Mahaweli Ganga) | -2.23 | 🟢 Normal | 0.182 | 🔺 Rising |
| 2026-03-13 11:05:57 | Panadugama (Nilwala Ganga) | 2.69 | 🟢 Normal | 0.075 | 🔺 Rising |
| 2026-03-13 12:01:07 | Ellagawa (Kalu Ganga) | 4.22 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-03-13 11:01:46 | Nagalagam Street (Kelani Ganga) | 0.34 | 🟢 Normal | 0.033 | 🔺 Rising |
| 2026-03-13 12:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.67 | 🟢 Normal | 0.012 | 🔺 Rising |
| 2026-03-13 11:02:51 | Wellawaya (Kirindi Oya) | 0.70 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-03-13 11:19:43 | Moragaswewa (Deduru Oya) | -0.05 | 🟢 Normal | 0.000 |  |
| 2026-03-13 12:01:23 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:05:40 | Giriulla (Maha Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-13 12:01:22 | Horowpothana (Yan Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:01:08 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:22:04 | Baddegama (Gin Ganga) | 1.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:01:14 | Padiyathalawa (Maduru Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:04:38 | Moraketiya (Walawe Ganga) | 1.00 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:02:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:10:53 | Dunamale (Aththanagalu Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:05:52 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:00:57 | Thanthirimale (Malwathu Oya) | 1.07 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:13:29 | Thalgahagoda (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:03:06 | Kuda Oya (Kirindi Oya) | 1.04 | 🟢 Normal | 0.000 |  |
| 2026-03-13 11:02:02 | Nakkala (Kumbukkan Oya) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-03-13 11:07:33 | Holombuwa (Kelani Ganga) | 0.27 | 🟢 Normal | -0.010 |  |
| 2026-03-13 11:02:33 | Putupaula (Kalu Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-03-13 12:00:27 | Thaldena (Mahaweli Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-13 11:00:55 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | -0.010 |  |
| 2026-03-13 11:01:21 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | -0.011 |  |
| 2026-03-13 11:06:50 | Magura (Kalu Ganga) | 1.06 | 🟢 Normal | -0.011 |  |
| 2026-03-13 11:03:19 | Katharagama (Menik Ganga) | -0.21 | 🟢 Normal | -0.011 |  |
| 2026-03-13 11:04:22 | Manampitiya (Mahaweli Ganga) | 0.38 | 🟢 Normal | -0.019 |  |
| 2026-03-13 11:03:16 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2026-03-13 11:03:49 | Hanwella (Kelani Ganga) | 0.84 | 🟢 Normal | -0.030 |  |
| 2026-03-13 11:05:32 | Peradeniya (Mahaweli Ganga) | 1.32 | 🟢 Normal | -0.030 |  |
| 2026-03-13 11:04:37 | Rathnapura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.036 |  |
| 2026-03-13 11:04:09 | Deraniyagala (Kelani Ganga) | 0.35 | 🟢 Normal | -0.039 |  |
| 2026-03-13 11:02:25 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.74 | 🟢 Normal | -0.040 |  |
| 2026-03-13 11:03:37 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | -0.041 |  |
| 2026-03-13 11:06:23 | Thawalama (Gin Ganga) | 1.90 | 🟢 Normal | -0.041 |  |
| 2026-03-13 11:03:19 | Glencourse (Kelani Ganga) | 8.74 | 🟢 Normal | -0.072 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

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

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)