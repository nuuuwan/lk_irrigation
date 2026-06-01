# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--01_10:12:47-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **167,412 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **13** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 10:12:47 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:12:41 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:12:31 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:10:02 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:09:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:09:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-01 10:07:55 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.018 |  |
| 2026-06-01 10:07:28 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.245 |  |
| 2026-06-01 10:07:12 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:06:26 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:06:16 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.028 |  |
| 2026-06-01 10:06:10 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-01 10:06:06 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-01 10:06:10 | Thalgahagoda (Nilwala Ganga) | 0.28 | 🟢 Normal | 0.041 | 🔺 Rising |
| 2026-06-01 10:09:36 | Nagalagam Street (Kelani Ganga) | 0.30 | 🟢 Normal | 0.028 | 🔺 Rising |
| 2026-06-01 10:03:15 | Siyambalanduwa (Heda Oya) | 0.42 | 🟢 Normal | 0.011 | 🔺 Rising |
| 2026-06-01 10:01:56 | Nakkala (Kumbukkan Oya) | 0.65 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:04:02 | Moragaswewa (Deduru Oya) | 0.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:01:44 | Nawalapitiya (Mahaweli Ganga) | 1.24 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:09:39 | Yaka Wewa (Ma Oya) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:02:01 | Giriulla (Maha Oya) | 1.01 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:00:47 | Horowpothana (Yan Oya) | 1.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:06:26 | Galgamuwa (Mee Oya) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:12:41 | Padiyathalawa (Maduru Oya) | 0.11 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:12:31 | Glencourse (Kelani Ganga) | 10.05 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:04:22 | Moraketiya (Walawe Ganga) | 0.87 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:12:47 | Dunamale (Aththanagalu Oya) | 1.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:03:58 | Thaldena (Mahaweli Ganga) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:02:13 | Katharagama (Menik Ganga) | -0.12 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:05:25 | Badalgama (Maha Oya) | 2.15 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:00:34 | Thanthirimale (Malwathu Oya) | 1.29 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:07:12 | Thawalama (Gin Ganga) | 1.74 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:06:06 | Peradeniya (Mahaweli Ganga) | 1.38 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:05:29 | Urawa (Nilwala Ganga) | 0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:04:22 | Kuda Oya (Kirindi Oya) | 1.27 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:02:41 | Thanamalwila (Kirindi Oya) | 0.63 | 🟢 Normal | 0.000 |  |
| 2026-06-01 10:10:02 | Rathnapura (Kalu Ganga) | 1.63 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:01:45 | Ellagawa (Kalu Ganga) | 5.54 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:02:30 | Norwood (Kelani Ganga) | 0.54 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:01:26 | Weraganthota (Mahaweli Ganga) | -3.26 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:02:55 | Magura (Kalu Ganga) | 1.99 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:02:01 | Pitabeddara (Nilwala Ganga) | 0.64 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:04:51 | Panadugama (Nilwala Ganga) | 2.65 | 🟢 Normal | -0.010 |  |
| 2026-06-01 10:07:55 | Manampitiya (Mahaweli Ganga) | -0.07 | 🟢 Normal | -0.018 |  |
| 2026-06-01 10:02:53 | Deraniyagala (Kelani Ganga) | 0.91 | 🟢 Normal | -0.020 |  |
| 2026-06-01 10:06:16 | Holombuwa (Kelani Ganga) | 0.46 | 🟢 Normal | -0.028 |  |
| 2026-06-01 10:02:20 | Kalawellawa (Millakanda) (Kalu Ganga) | 3.47 | 🟢 Normal | -0.030 |  |
| 2026-06-01 10:03:07 | Hanwella (Kelani Ganga) | 1.98 | 🟢 Normal | -0.031 |  |
| 2026-06-01 10:02:59 | Baddegama (Gin Ganga) | 1.97 | 🟢 Normal | -0.049 |  |
| 2026-06-01 09:05:10 | Wellawaya (Kirindi Oya) | 0.86 | 🟢 Normal | -0.067 |  |
| 2026-06-01 10:03:37 | Putupaula (Kalu Ganga) | 0.69 | 🟢 Normal | -0.080 |  |
| 2026-06-01 10:07:28 | Kithulgala (Kelani Ganga) | 1.35 | 🟢 Normal | -0.245 |  |

## River Water Level Charts by Station

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

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

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)