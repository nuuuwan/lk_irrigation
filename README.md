# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--24_15:03:14-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **81,864 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **23** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 15:03:14 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-24 15:03:03 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:33 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:31 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-24 15:02:28 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:18 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:17 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:02 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.204 |  |
| 2026-02-24 15:02:02 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:00 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-24 15:01:51 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:01:41 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-02-24 15:01:33 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-24 15:01:16 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:01:15 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:01:14 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:00:41 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:14:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:13:52 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-02-24 14:08:05 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.041 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-24 15:02:00 | Putupaula (Kalu Ganga) | 0.43 | 🟢 Normal | 0.093 | 🔺 Rising |
| 2026-02-24 15:01:33 | Nagalagam Street (Kelani Ganga) | 0.47 | 🟢 Normal | 0.076 | 🔺 Rising |
| 2026-02-24 14:03:34 | Thawalama (Gin Ganga) | 1.19 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-02-24 14:03:18 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-02-24 15:02:31 | Siyambalanduwa (Heda Oya) | 0.62 | 🟢 Normal | 0.019 | 🔺 Rising |
| 2026-02-24 14:04:55 | Galgamuwa (Mee Oya) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-24 15:02:02 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:28 | Moragaswewa (Deduru Oya) | 0.01 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:19 | Nawalapitiya (Mahaweli Ganga) | 0.70 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:01:15 | Yaka Wewa (Ma Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:01:51 | Pitabeddara (Nilwala Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:02:30 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:24 | Ellagawa (Kalu Ganga) | 4.40 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:44 | Panadugama (Nilwala Ganga) | 2.24 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:01:57 | Dunamale (Aththanagalu Oya) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:06:07 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:03:03 | Badalgama (Maha Oya) | 1.97 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:07:32 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:01:14 | Manampitiya (Mahaweli Ganga) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:14:30 | Urawa (Nilwala Ganga) | 0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-24 15:02:12 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.14 | 🟢 Normal | 0.000 |  |
| 2026-02-24 14:05:42 | Padiyathalawa (Maduru Oya) | 1.04 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:17 | Horowpothana (Yan Oya) | 1.78 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:04:30 | Giriulla (Maha Oya) | 0.88 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:19 | Thanthirimale (Malwathu Oya) | 1.57 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:59 | Moraketiya (Walawe Ganga) | 0.81 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:03:00 | Deraniyagala (Kelani Ganga) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:04:01 | Hanwella (Kelani Ganga) | 0.52 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:33 | Magura (Kalu Ganga) | 1.16 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:00:41 | Kuda Oya (Kirindi Oya) | 1.37 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:02:18 | Nakkala (Kumbukkan Oya) | 1.00 | 🟢 Normal | -0.010 |  |
| 2026-02-24 15:01:16 | Thaldena (Mahaweli Ganga) | 0.56 | 🟢 Normal | -0.010 |  |
| 2026-02-24 14:02:42 | Baddegama (Gin Ganga) | 0.80 | 🟢 Normal | -0.011 |  |
| 2026-02-24 14:04:38 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | -0.011 |  |
| 2026-02-24 15:01:41 | Wellawaya (Kirindi Oya) | 1.13 | 🟢 Normal | -0.020 |  |
| 2026-02-24 15:03:14 | Thanamalwila (Kirindi Oya) | 1.16 | 🟢 Normal | -0.020 |  |
| 2026-02-24 14:13:52 | Thalgahagoda (Nilwala Ganga) | 0.18 | 🟢 Normal | -0.038 |  |
| 2026-02-24 14:08:05 | Glencourse (Kelani Ganga) | 8.53 | 🟢 Normal | -0.041 |  |
| 2026-02-24 15:02:02 | Weraganthota (Mahaweli Ganga) | -2.17 | 🟢 Normal | -0.204 |  |

## River Water Level Charts by Station

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)