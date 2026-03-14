# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--14_05:27:05-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **96,837 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **34** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 05:27:05 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:22:01 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 1.029 | 🔺 Rising |
| 2026-03-14 05:21:26 | Rathnapura (Kalu Ganga) | 1.18 | 🟢 Normal | 1.029 | 🔺 Rising |
| 2026-03-14 05:13:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:11:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-03-14 05:09:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:07:32 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-14 05:07:10 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.147 |  |
| 2026-03-14 05:06:31 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:06:25 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:06:24 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-14 05:05:27 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-14 05:04:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.005 |  |
| 2026-03-14 05:04:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 05:04:14 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-14 05:03:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.133 |  |
| 2026-03-14 05:03:22 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-03-14 05:03:08 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 05:03:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-03-14 05:02:51 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:02:43 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:02:32 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.020 |  |
| 2026-03-14 05:02:23 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 05:02:21 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.201 |  |
| 2026-03-14 05:02:14 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:02:13 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:01:53 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:01:27 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-14 05:01:24 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.055 |  |
| 2026-03-14 05:01:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:01:03 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.136 |  |
| 2026-03-14 05:00:31 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 05:00:16 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-14 05:22:01 | Rathnapura (Kalu Ganga) | 1.19 | 🟢 Normal | 1.029 | 🔺 Rising |
| 2026-03-14 05:06:24 | Moragaswewa (Deduru Oya) | 0.08 | 🟢 Normal | 0.110 | 🔺 Rising |
| 2026-03-14 05:11:05 | Putupaula (Kalu Ganga) | 0.55 | 🟢 Normal | 0.082 | 🔺 Rising |
| 2026-03-14 04:25:46 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.37 | 🟢 Normal | 0.079 | 🔺 Rising |
| 2026-03-14 05:04:14 | Deraniyagala (Kelani Ganga) | 0.34 | 🟢 Normal | 0.050 | 🔺 Rising |
| 2026-03-14 05:01:27 | Glencourse (Kelani Ganga) | 9.15 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-03-14 05:00:31 | Wellawaya (Kirindi Oya) | 0.80 | 🟢 Normal | 0.040 | 🔺 Rising |
| 2026-03-14 05:04:15 | Giriulla (Maha Oya) | 1.00 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 05:02:23 | Manampitiya (Mahaweli Ganga) | 0.42 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 05:03:08 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-14 05:00:16 | Thalgahagoda (Nilwala Ganga) | 0.55 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-03-14 05:04:16 | Kuda Oya (Kirindi Oya) | 1.09 | 🟢 Normal | 0.005 |  |
| 2026-03-14 05:01:18 | Nakkala (Kumbukkan Oya) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:02:14 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-13 23:00:33 | Horowpothana (Yan Oya) | 1.26 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:03:14 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:06:31 | Magura (Kalu Ganga) | 0.96 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:02:13 | Pitabeddara (Nilwala Ganga) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:06:25 | Baddegama (Gin Ganga) | 1.35 | 🟢 Normal | 0.000 |  |
| 2026-03-14 04:01:12 | Padiyathalawa (Maduru Oya) | 0.46 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:09:07 | Nagalagam Street (Kelani Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:01:53 | Siyambalanduwa (Heda Oya) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:13:53 | Dunamale (Aththanagalu Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:02:43 | Thaldena (Mahaweli Ganga) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:03:02 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:02:51 | Badalgama (Maha Oya) | 1.73 | 🟢 Normal | 0.000 |  |
| 2026-03-13 18:02:59 | Thanthirimale (Malwathu Oya) | 1.06 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:27:05 | Thanamalwila (Kirindi Oya) | 0.33 | 🟢 Normal | 0.000 |  |
| 2026-03-14 05:05:27 | Hanwella (Kelani Ganga) | 0.82 | 🟢 Normal | -0.010 |  |
| 2026-03-14 05:02:32 | Ellagawa (Kalu Ganga) | 4.29 | 🟢 Normal | -0.020 |  |
| 2026-03-14 05:07:32 | Holombuwa (Kelani Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-03-14 05:03:22 | Norwood (Kelani Ganga) | 0.52 | 🟢 Normal | -0.023 |  |
| 2026-03-14 05:03:01 | Nawalapitiya (Mahaweli Ganga) | 0.75 | 🟢 Normal | -0.039 |  |
| 2026-03-14 05:01:24 | Panadugama (Nilwala Ganga) | 2.35 | 🟢 Normal | -0.055 |  |
| 2026-03-13 18:03:30 | Weraganthota (Mahaweli Ganga) | -2.94 | 🟢 Normal | -0.078 |  |
| 2026-03-14 05:03:25 | Peradeniya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.133 |  |
| 2026-03-14 05:01:03 | Thawalama (Gin Ganga) | 1.80 | 🟢 Normal | -0.136 |  |
| 2026-03-14 05:07:10 | Urawa (Nilwala Ganga) | 0.01 | 🟢 Normal | -0.147 |  |
| 2026-03-14 05:02:21 | Kithulgala (Kelani Ganga) | 1.32 | 🟢 Normal | -0.201 |  |

## River Water Level Charts by Station

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)