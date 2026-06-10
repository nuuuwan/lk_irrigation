# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--10_07:40:12-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **175,348 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **8** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 07:40:12 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:32:53 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:29:19 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:22:55 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-06-10 07:15:51 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:13:32 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-10 07:10:06 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.009 |  |
| 2026-06-10 07:09:40 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.015 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-10 07:02:30 | Nagalagam Street (Kelani Ganga) | 0.64 | 🟢 Normal | 0.101 | 🔺 Rising |
| 2026-06-10 07:13:32 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.045 | 🔺 Rising |
| 2026-06-10 07:02:38 | Deraniyagala (Kelani Ganga) | 1.25 | 🟢 Normal | 0.030 | 🔺 Rising |
| 2026-06-10 07:05:00 | Magura (Kalu Ganga) | 2.20 | 🟢 Normal | 0.029 | 🔺 Rising |
| 2026-06-10 07:01:52 | Wellawaya (Kirindi Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:02:09 | Nakkala (Kumbukkan Oya) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:03:53 | Moragaswewa (Deduru Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:00:12 | Nawalapitiya (Mahaweli Ganga) | 1.63 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:01:56 | Yaka Wewa (Ma Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:01:07 | Horowpothana (Yan Oya) | 1.28 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:29:19 | Pitabeddara (Nilwala Ganga) | 0.62 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:04:36 | Norwood (Kelani Ganga) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:32:53 | Panadugama (Nilwala Ganga) | 2.67 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:03:47 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:01:22 | Moraketiya (Walawe Ganga) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:00:38 | Siyambalanduwa (Heda Oya) | 0.41 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:15:51 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:40:12 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:01:25 | Kuda Oya (Kirindi Oya) | 1.19 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:02:22 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-10 07:00:57 | Galgamuwa (Mee Oya) | 0.28 | 🟢 Normal | -0.002 |  |
| 2026-06-10 07:22:55 | Thanthirimale (Malwathu Oya) | 1.26 | 🟢 Normal | -0.005 |  |
| 2026-06-10 07:10:06 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | -0.009 |  |
| 2026-06-10 07:04:38 | Rathnapura (Kalu Ganga) | 1.70 | 🟢 Normal | -0.010 |  |
| 2026-06-10 07:05:27 | Thalgahagoda (Nilwala Ganga) | 0.33 | 🟢 Normal | -0.010 |  |
| 2026-06-10 07:03:31 | Thaldena (Mahaweli Ganga) | 0.17 | 🟢 Normal | -0.010 |  |
| 2026-06-10 07:02:33 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.69 | 🟢 Normal | -0.011 |  |
| 2026-06-10 07:09:40 | Putupaula (Kalu Ganga) | 0.97 | 🟢 Normal | -0.015 |  |
| 2026-06-10 07:04:41 | Badalgama (Maha Oya) | 2.60 | 🟢 Normal | -0.019 |  |
| 2026-06-10 07:04:21 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.020 |  |
| 2026-06-10 07:02:09 | Baddegama (Gin Ganga) | 1.85 | 🟢 Normal | -0.021 |  |
| 2026-06-10 07:06:06 | Peradeniya (Mahaweli Ganga) | 1.95 | 🟢 Normal | -0.030 |  |
| 2026-06-10 07:01:53 | Thawalama (Gin Ganga) | 1.77 | 🟢 Normal | -0.032 |  |
| 2026-06-10 07:06:19 | Glencourse (Kelani Ganga) | 10.85 | 🟢 Normal | -0.038 |  |
| 2026-06-10 07:05:11 | Hanwella (Kelani Ganga) | 2.90 | 🟢 Normal | -0.038 |  |
| 2026-06-10 07:04:43 | Dunamale (Aththanagalu Oya) | 1.84 | 🟢 Normal | -0.038 |  |
| 2026-06-10 07:03:43 | Manampitiya (Mahaweli Ganga) | -0.02 | 🟢 Normal | -0.059 |  |
| 2026-06-10 07:05:52 | Weraganthota (Mahaweli Ganga) | -3.18 | 🟢 Normal | -0.074 |  |
| 2026-06-10 07:00:40 | Kithulgala (Kelani Ganga) | 1.80 | 🟢 Normal | -0.202 |  |

## River Water Level Charts by Station

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)