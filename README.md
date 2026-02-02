# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--02_14:11:56-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **62,512 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **41** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 14:11:56 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:11:18 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:10:14 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-02-02 14:07:34 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-02 14:07:00 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-02-02 14:06:17 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:05:44 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-02-02 14:05:04 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:05 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-02-02 14:03:57 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-02-02 14:03:42 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.005 |  |
| 2026-02-02 14:03:31 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:03:18 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:03:11 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-02-02 14:02:57 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 14:02:26 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-02-02 14:02:26 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.021 |  |
| 2026-02-02 14:02:23 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:02:16 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:02:13 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:59 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:53 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:51 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.147 |  |
| 2026-02-02 14:01:41 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.060 |  |
| 2026-02-02 14:01:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 14:01:23 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 14:01:18 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-02-02 14:01:18 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:04 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:00:51 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:00:46 | Thanthirimale (Malwathu Oya) | 2.49 | 🟢 Normal | -0.064 |  |
| 2026-02-02 14:00:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 13:29:39 | Thalgahagoda (Nilwala Ganga) | 0.14 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-02-02 13:27:51 | Thalgahagoda (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-02-02 13:23:03 | Thanthirimale (Malwathu Oya) | 2.53 | 🟢 Normal | -0.064 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-02 14:03:57 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | 0.332 | 🔺 Rising |
| 2026-02-02 14:02:26 | Putupaula (Kalu Ganga) | 0.65 | 🟢 Normal | 0.154 | 🔺 Rising |
| 2026-02-02 14:01:33 | Nagalagam Street (Kelani Ganga) | 0.58 | 🟢 Normal | 0.031 | 🔺 Rising |
| 2026-02-02 14:02:57 | Deraniyagala (Kelani Ganga) | 0.10 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 14:01:23 | Moragaswewa (Deduru Oya) | 0.27 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-02-02 14:02:13 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:02:16 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:00:05 | Nakkala (Kumbukkan Oya) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:06 | Nawalapitiya (Mahaweli Ganga) | 0.69 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:30 | Giriulla (Maha Oya) | 0.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:53 | Horowpothana (Yan Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:06:17 | Galgamuwa (Mee Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:11:56 | Magura (Kalu Ganga) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:02:23 | Norwood (Kelani Ganga) | 0.42 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:13 | Hanwella (Kelani Ganga) | 0.44 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:11:18 | Panadugama (Nilwala Ganga) | 2.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:00:51 | Padiyathalawa (Maduru Oya) | 0.66 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:18 | Glencourse (Kelani Ganga) | 8.50 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:59 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:05 | Siyambalanduwa (Heda Oya) | 0.57 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:01:04 | Thaldena (Mahaweli Ganga) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:03:31 | Badalgama (Maha Oya) | 1.90 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:05:04 | Holombuwa (Kelani Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:05 | Kuda Oya (Kirindi Oya) | 1.22 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:03:18 | Thanamalwila (Kirindi Oya) | 0.49 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:04:23 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.72 | 🟢 Normal | 0.000 |  |
| 2026-02-02 14:03:42 | Urawa (Nilwala Ganga) | 0.14 | 🟢 Normal | -0.005 |  |
| 2026-02-02 14:10:14 | Dunamale (Aththanagalu Oya) | 0.74 | 🟢 Normal | -0.009 |  |
| 2026-02-02 14:05:44 | Manampitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.009 |  |
| 2026-02-02 14:07:34 | Katharagama (Menik Ganga) | -0.05 | 🟢 Normal | -0.010 |  |
| 2026-02-02 14:03:11 | Yaka Wewa (Ma Oya) | 1.06 | 🟢 Normal | -0.020 |  |
| 2026-02-02 14:01:18 | Pitabeddara (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.021 |  |
| 2026-02-02 14:02:26 | Ellagawa (Kalu Ganga) | 4.38 | 🟢 Normal | -0.021 |  |
| 2026-02-02 14:04:03 | Thawalama (Gin Ganga) | 1.02 | 🟢 Normal | -0.021 |  |
| 2026-02-02 14:07:00 | Baddegama (Gin Ganga) | 1.04 | 🟢 Normal | -0.039 |  |
| 2026-02-02 12:09:30 | Rathnapura (Kalu Ganga) | 0.89 | 🟢 Normal | -0.045 |  |
| 2026-02-02 14:01:41 | Weraganthota (Mahaweli Ganga) | -2.30 | 🟢 Normal | -0.060 |  |
| 2026-02-02 14:00:46 | Thanthirimale (Malwathu Oya) | 2.49 | 🟢 Normal | -0.064 |  |
| 2026-02-02 14:01:51 | Peradeniya (Mahaweli Ganga) | 1.31 | 🟢 Normal | -0.147 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

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

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)