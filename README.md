# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--03--12_11:15:16-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **95,294 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 11:15:16 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:14:23 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 5.453 | 🔺 Rising |
| 2026-03-12 11:11:13 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:10:52 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:10:05 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:10:03 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:09:20 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-12 11:07:18 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-12 11:06:15 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:06:14 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:05:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-03-12 11:04:33 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:04:15 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-12 11:04:12 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-12 11:03:59 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-12 11:03:52 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:03:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-03-12 11:03:35 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:03:18 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-03-12 11:03:09 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:52 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-12 11:02:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:33 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.086 |  |
| 2026-03-12 11:02:30 | Thalgahagoda (Nilwala Ganga) | 0.20 | 🟢 Normal | 5.453 | 🔺 Rising |
| 2026-03-12 11:02:28 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-03-12 11:02:08 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:07 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-12 11:02:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:55 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-03-12 11:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:40 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:27 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:14 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-12 11:01:11 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:11 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:00:59 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:00:38 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:42:26 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.006 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-03-12 11:14:23 | Thalgahagoda (Nilwala Ganga) | 1.28 | 🟢 Normal | 5.453 | 🔺 Rising |
| 2026-03-12 11:03:47 | Kithulgala (Kelani Ganga) | 1.43 | 🟢 Normal | 0.175 | 🔺 Rising |
| 2026-03-12 11:02:07 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | 0.156 | 🔺 Rising |
| 2026-03-12 11:07:18 | Panadugama (Nilwala Ganga) | 1.98 | 🟢 Normal | 0.095 | 🔺 Rising |
| 2026-03-12 11:04:12 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-12 11:01:14 | Pitabeddara (Nilwala Ganga) | 0.69 | 🟢 Normal | 0.063 | 🔺 Rising |
| 2026-03-12 11:03:59 | Peradeniya (Mahaweli Ganga) | 1.30 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2026-03-12 11:02:28 | Wellawaya (Kirindi Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:01 | Nakkala (Kumbukkan Oya) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:00:38 | Moragaswewa (Deduru Oya) | -0.02 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:44 | Yaka Wewa (Ma Oya) | 0.60 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:03:52 | Giriulla (Maha Oya) | 0.64 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:11 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:11:13 | Galgamuwa (Mee Oya) | -0.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:10:03 | Magura (Kalu Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:03:35 | Norwood (Kelani Ganga) | 0.36 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:03:09 | Hanwella (Kelani Ganga) | 1.09 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:27 | Ellagawa (Kalu Ganga) | 3.76 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:11 | Padiyathalawa (Maduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:04:33 | Nagalagam Street (Kelani Ganga) | 0.27 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:47 | Siyambalanduwa (Heda Oya) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:00:59 | Dunamale (Aththanagalu Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:40 | Thaldena (Mahaweli Ganga) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:09 | Katharagama (Menik Ganga) | -0.23 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:06:15 | Badalgama (Maha Oya) | 1.70 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:10:52 | Rathnapura (Kalu Ganga) | 0.47 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:01:51 | Thanthirimale (Malwathu Oya) | 1.08 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:15:16 | Urawa (Nilwala Ganga) | 0.34 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:06:14 | Kuda Oya (Kirindi Oya) | 1.03 | 🟢 Normal | 0.000 |  |
| 2026-03-12 11:02:08 | Thanamalwila (Kirindi Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-03-12 10:42:26 | Thawalama (Gin Ganga) | 1.18 | 🟢 Normal | -0.006 |  |
| 2026-03-12 11:09:20 | Baddegama (Gin Ganga) | 1.07 | 🟢 Normal | -0.010 |  |
| 2026-03-12 11:02:52 | Moraketiya (Walawe Ganga) | 0.51 | 🟢 Normal | -0.010 |  |
| 2026-03-12 11:04:15 | Putupaula (Kalu Ganga) | 0.33 | 🟢 Normal | -0.020 |  |
| 2026-03-12 11:02:08 | Nawalapitiya (Mahaweli Ganga) | 0.63 | 🟢 Normal | -0.020 |  |
| 2026-03-12 11:01:55 | Manampitiya (Mahaweli Ganga) | 0.44 | 🟢 Normal | -0.032 |  |
| 2026-03-12 11:05:35 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.38 | 🟢 Normal | -0.039 |  |
| 2026-03-12 11:03:18 | Deraniyagala (Kelani Ganga) | 0.13 | 🟢 Normal | -0.040 |  |
| 2026-03-12 11:02:33 | Glencourse (Kelani Ganga) | 8.92 | 🟢 Normal | -0.086 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

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

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

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

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)