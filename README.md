# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--15_16:06:30-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **180,165 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **31** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 16:06:30 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:05:44 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:05:41 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:05:41 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-06-15 16:05:33 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.058 |  |
| 2026-06-15 16:05:29 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:04:51 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:04:32 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:04:08 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:03:31 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:02:56 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.042 |  |
| 2026-06-15 16:02:54 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:02:52 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.021 |  |
| 2026-06-15 16:02:47 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-15 16:02:46 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 16:02:31 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-06-15 16:02:21 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:02:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-15 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -0.090 |  |
| 2026-06-15 16:02:12 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:02:07 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:02:03 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-06-15 16:02:01 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-15 16:01:53 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:01:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:01:38 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:01:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:00:47 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:00:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-15 16:02:47 | Deraniyagala (Kelani Ganga) | 1.03 | 🟢 Normal | 0.060 | 🔺 Rising |
| 2026-06-15 16:02:14 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-15 16:02:46 | Manampitiya (Mahaweli Ganga) | -0.12 | 🟢 Normal | 0.010 | 🔺 Rising |
| 2026-06-15 16:00:19 | Weraganthota (Mahaweli Ganga) | -3.36 | 🟢 Normal | 0.000 |  |
| 2026-06-15 15:03:17 | Moragaswewa (Deduru Oya) | 0.73 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:01:42 | Yaka Wewa (Ma Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:01:53 | Pitabeddara (Nilwala Ganga) | 0.68 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:03:31 | Hanwella (Kelani Ganga) | 2.56 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:04:51 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-15 15:05:23 | Nagalagam Street (Kelani Ganga) | 0.94 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:01:15 | Siyambalanduwa (Heda Oya) | 0.43 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:04:32 | Holombuwa (Kelani Ganga) | 0.75 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:02:21 | Thawalama (Gin Ganga) | 1.92 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:05:44 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-15 15:03:24 | Thalgahagoda (Nilwala Ganga) | 0.38 | 🟢 Normal | 0.000 |  |
| 2026-06-15 16:02:07 | Thanamalwila (Kirindi Oya) | 0.40 | 🟢 Normal | 0.000 |  |
| 2026-06-15 15:06:44 | Kithulgala (Kelani Ganga) | 1.69 | 🟢 Normal | -0.005 |  |
| 2026-06-15 16:06:30 | Galgamuwa (Mee Oya) | 0.48 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:05:29 | Panadugama (Nilwala Ganga) | 2.88 | 🟢 Normal | -0.010 |  |
| 2026-06-15 15:05:53 | Moraketiya (Walawe Ganga) | 0.90 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:05:41 | Rathnapura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:00:47 | Horowpothana (Yan Oya) | 1.52 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:02:54 | Norwood (Kelani Ganga) | 0.75 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:01:41 | Wellawaya (Kirindi Oya) | 0.57 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:00:24 | Nakkala (Kumbukkan Oya) | 0.61 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:02:12 | Giriulla (Maha Oya) | 1.38 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:04:08 | Badalgama (Maha Oya) | 2.66 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:01:38 | Katharagama (Menik Ganga) | -0.16 | 🟢 Normal | -0.010 |  |
| 2026-06-15 15:02:26 | Nawalapitiya (Mahaweli Ganga) | 1.50 | 🟢 Normal | -0.010 |  |
| 2026-06-15 16:02:03 | Thanthirimale (Malwathu Oya) | 1.42 | 🟢 Normal | -0.011 |  |
| 2026-06-15 16:02:01 | Kuda Oya (Kirindi Oya) | 1.18 | 🟢 Normal | -0.020 |  |
| 2026-06-15 16:05:41 | Baddegama (Gin Ganga) | 1.99 | 🟢 Normal | -0.020 |  |
| 2026-06-15 16:02:31 | Magura (Kalu Ganga) | 2.10 | 🟢 Normal | -0.020 |  |
| 2026-06-15 16:02:52 | Putupaula (Kalu Ganga) | 1.75 | 🟢 Normal | -0.021 |  |
| 2026-06-15 15:04:05 | Peradeniya (Mahaweli Ganga) | 1.78 | 🟢 Normal | -0.025 |  |
| 2026-06-15 16:02:56 | Glencourse (Kelani Ganga) | 10.53 | 🟢 Normal | -0.042 |  |
| 2026-06-15 16:05:33 | Ellagawa (Kalu Ganga) | 6.04 | 🟢 Normal | -0.058 |  |
| 2026-06-15 15:03:52 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.063 |  |
| 2026-06-15 16:02:14 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.53 | 🟢 Normal | -0.090 |  |

## River Water Level Charts by Station

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)