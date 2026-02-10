# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--02--10_22:12:39-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **69,616 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **32** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 22:12:39 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:09:54 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:09:45 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-02-10 22:09:06 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:07:34 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:07:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:07:15 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.319 |  |
| 2026-02-10 22:06:45 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:05:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-02-10 22:05:19 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:05:17 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:05:05 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:04:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:04:26 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:04:02 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:45 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:25 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:20 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:08 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:08 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.095 |  |
| 2026-02-10 22:02:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:02:50 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2026-02-10 22:02:33 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:02:30 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-02-10 22:02:17 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-02-10 22:02:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-10 22:02:08 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:01:12 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-10 22:01:04 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:01:02 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-02-10 22:00:10 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-02-10 22:01:02 | Peradeniya (Mahaweli Ganga) | 1.72 | 🟢 Normal | 0.454 | 🔺 Rising |
| 2026-02-10 21:00:18 | Thaldena (Mahaweli Ganga) | 0.77 | 🟢 Normal | 0.306 | 🔺 Rising |
| 2026-02-10 18:04:12 | Weraganthota (Mahaweli Ganga) | -2.73 | 🟢 Normal | 0.057 | 🔺 Rising |
| 2026-02-10 22:00:10 | Wellawaya (Kirindi Oya) | 0.88 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:01:04 | Nakkala (Kumbukkan Oya) | 0.86 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:02:33 | Moragaswewa (Deduru Oya) | 0.19 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:20 | Nawalapitiya (Mahaweli Ganga) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:02:08 | Yaka Wewa (Ma Oya) | 0.67 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:05:17 | Giriulla (Maha Oya) | 0.71 | 🟢 Normal | 0.000 |  |
| 2026-02-10 18:03:04 | Galgamuwa (Mee Oya) | 0.22 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:20:37 | Magura (Kalu Ganga) | 0.76 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:08 | Pitabeddara (Nilwala Ganga) | 0.26 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:05:19 | Deraniyagala (Kelani Ganga) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:04:02 | Ellagawa (Kalu Ganga) | 3.85 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:06:45 | Baddegama (Gin Ganga) | 1.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 20:03:41 | Panadugama (Nilwala Ganga) | 2.25 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:25 | Padiyathalawa (Maduru Oya) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:05:05 | Glencourse (Kelani Ganga) | 8.21 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:04:26 | Moraketiya (Walawe Ganga) | 0.82 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:04:53 | Siyambalanduwa (Heda Oya) | 0.52 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:07:34 | Dunamale (Aththanagalu Oya) | 0.12 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:02:59 | Katharagama (Menik Ganga) | -0.08 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:07:23 | Badalgama (Maha Oya) | 1.80 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:09:54 | Holombuwa (Kelani Ganga) | 0.32 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:09:06 | Rathnapura (Kalu Ganga) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:12:39 | Thawalama (Gin Ganga) | 0.97 | 🟢 Normal | 0.000 |  |
| 2026-02-10 21:02:46 | Urawa (Nilwala Ganga) | 0.04 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:03:58 | Kuda Oya (Kirindi Oya) | 1.16 | 🟢 Normal | 0.000 |  |
| 2026-02-10 22:09:45 | Thanamalwila (Kirindi Oya) | 0.45 | 🟢 Normal | -0.009 |  |
| 2026-02-10 22:01:12 | Horowpothana (Yan Oya) | 1.45 | 🟢 Normal | -0.010 |  |
| 2026-02-10 18:01:05 | Thanthirimale (Malwathu Oya) | 1.27 | 🟢 Normal | -0.010 |  |
| 2026-02-10 22:02:17 | Norwood (Kelani Ganga) | 0.40 | 🟢 Normal | -0.010 |  |
| 2026-02-10 22:02:50 | Manampitiya (Mahaweli Ganga) | 0.60 | 🟢 Normal | -0.021 |  |
| 2026-02-10 22:02:30 | Hanwella (Kelani Ganga) | 0.38 | 🟢 Normal | -0.021 |  |
| 2026-02-10 21:02:01 | Kalawellawa (Millakanda) (Kalu Ganga) | 1.40 | 🟢 Normal | -0.023 |  |
| 2026-02-10 22:02:17 | Thalgahagoda (Nilwala Ganga) | 0.36 | 🟢 Normal | -0.029 |  |
| 2026-02-10 22:05:34 | Nagalagam Street (Kelani Ganga) | 0.37 | 🟢 Normal | -0.060 |  |
| 2026-02-10 22:03:08 | Putupaula (Kalu Ganga) | 0.56 | 🟢 Normal | -0.095 |  |
| 2026-02-10 22:07:15 | Kithulgala (Kelani Ganga) | 1.46 | 🟢 Normal | -0.319 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

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

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

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

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)