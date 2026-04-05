# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--04--05_18:10:08-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **117,058 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **39** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 18:10:08 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:08:44 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-05 18:07:02 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:06:26 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:06:04 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 18:05:38 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.020 |  |
| 2026-04-05 18:05:32 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-05 18:05:30 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:04:53 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:04:53 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-04-05 18:04:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.146 |  |
| 2026-04-05 18:04:26 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-05 18:04:22 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:03:57 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:03:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:03:42 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:03:33 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 18:03:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 18:02:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:02:37 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.040 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-05 18:02:25 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:24 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.017 |  |
| 2026-04-05 18:02:23 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 18:02:16 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-04-05 18:02:16 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.053 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-05 18:02:11 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:01:41 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:01:30 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 18:01:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:01:13 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.051 |  |
| 2026-04-05 18:01:11 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.041 |  |
| 2026-04-05 18:00:23 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.054 |  |
| 2026-04-05 18:00:09 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.040 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-04-05 18:04:53 | Kithulgala (Kelani Ganga) | 1.72 | 🟢 Normal | 0.325 | 🔺 Rising |
| 2026-04-05 18:08:44 | Rathnapura (Kalu Ganga) | 0.69 | 🟢 Normal | 0.066 | 🔺 Rising |
| 2026-04-05 18:02:16 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 18:00:09 | Thalgahagoda (Nilwala Ganga) | 0.58 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 18:03:11 | Thaldena (Mahaweli Ganga) | 0.30 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-04-05 18:04:26 | Baddegama (Gin Ganga) | 1.00 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-04-05 18:03:33 | Peradeniya (Mahaweli Ganga) | 1.16 | 🟢 Normal | 0.021 | 🔺 Rising |
| 2026-04-05 18:01:30 | Manampitiya (Mahaweli Ganga) | 0.86 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 18:02:23 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-04-05 18:06:04 | Katharagama (Menik Ganga) | 0.02 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-04-05 18:02:53 | Nakkala (Kumbukkan Oya) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:02:02 | Moragaswewa (Deduru Oya) | 0.00 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:03:53 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:03:42 | Norwood (Kelani Ganga) | 0.48 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:06:26 | Padiyathalawa (Maduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:04:22 | Dunamale (Aththanagalu Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:03:57 | Holombuwa (Kelani Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:04:53 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:01:41 | Thanamalwila (Kirindi Oya) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-04-05 18:10:08 | Panadugama (Nilwala Ganga) | 2.14 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:25 | Pitabeddara (Nilwala Ganga) | 0.43 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:01:37 | Nawalapitiya (Mahaweli Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:11 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:05:30 | Badalgama (Maha Oya) | 1.88 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:02:03 | Galgamuwa (Mee Oya) | 0.20 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:07:02 | Urawa (Nilwala Ganga) | -0.01 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:01:22 | Moraketiya (Walawe Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-04-05 18:05:32 | Magura (Kalu Ganga) | 0.81 | 🟢 Normal | -0.011 |  |
| 2026-04-05 18:02:24 | Giriulla (Maha Oya) | 0.84 | 🟢 Normal | -0.017 |  |
| 2026-04-05 18:05:38 | Glencourse (Kelani Ganga) | 8.38 | 🟢 Normal | -0.020 |  |
| 2026-04-05 18:02:16 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | -0.029 |  |
| 2026-04-05 18:02:37 | Thawalama (Gin Ganga) | 1.37 | 🟢 Normal | -0.040 |  |
| 2026-04-05 18:01:11 | Ellagawa (Kalu Ganga) | 4.30 | 🟢 Normal | -0.041 |  |
| 2026-04-05 18:02:13 | Weraganthota (Mahaweli Ganga) | -3.11 | 🟢 Normal | -0.050 |  |
| 2026-04-05 18:01:13 | Siyambalanduwa (Heda Oya) | 0.60 | 🟢 Normal | -0.051 |  |
| 2026-04-05 18:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.23 | 🟢 Normal | -0.053 |  |
| 2026-04-05 18:00:23 | Putupaula (Kalu Ganga) | 0.90 | 🟢 Normal | -0.054 |  |
| 2026-04-05 18:02:28 | Thanthirimale (Malwathu Oya) | 2.42 | 🟢 Normal | -0.088 |  |
| 2026-04-05 18:04:46 | Nagalagam Street (Kelani Ganga) | 0.67 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)