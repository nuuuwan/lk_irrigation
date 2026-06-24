# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2026--06--24_22:11:42-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **188,446 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **3** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 22:11:42 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.146 |  |
| 2026-06-24 22:09:38 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:08:59 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.046 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2026-06-24 22:02:53 | Peradeniya (Mahaweli Ganga) | 2.38 | 🟢 Normal | 0.280 | 🔺 Rising |
| 2026-06-24 22:01:32 | Wellawaya (Kirindi Oya) | 0.54 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:04:43 | Nakkala (Kumbukkan Oya) | 0.59 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:02:37 | Moragaswewa (Deduru Oya) | 0.51 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:01:59 | Yaka Wewa (Ma Oya) | 0.50 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:07:45 | Horowpothana (Yan Oya) | 1.36 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:21 | Galgamuwa (Mee Oya) | 0.45 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:04:46 | Pitabeddara (Nilwala Ganga) | 0.74 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:02:58 | Ellagawa (Kalu Ganga) | 5.80 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:02:05 | Padiyathalawa (Maduru Oya) | 0.07 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:05:54 | Nagalagam Street (Kelani Ganga) | 0.55 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:04:21 | Glencourse (Kelani Ganga) | 10.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:01:58 | Thaldena (Mahaweli Ganga) | 0.16 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:03:34 | Katharagama (Menik Ganga) | -0.13 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:02:38 | Manampitiya (Mahaweli Ganga) | -0.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 18:03:10 | Thanthirimale (Malwathu Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:09:38 | Urawa (Nilwala Ganga) | 0.30 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:03:37 | Kuda Oya (Kirindi Oya) | 1.14 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:02:17 | Thanamalwila (Kirindi Oya) | 0.37 | 🟢 Normal | 0.000 |  |
| 2026-06-24 22:07:44 | Moraketiya (Walawe Ganga) | 0.84 | 🟢 Normal | -0.009 |  |
| 2026-06-24 22:07:42 | Thawalama (Gin Ganga) | 1.73 | 🟢 Normal | -0.009 |  |
| 2026-06-24 22:05:27 | Baddegama (Gin Ganga) | 1.54 | 🟢 Normal | -0.009 |  |
| 2026-06-24 22:06:11 | Nawalapitiya (Mahaweli Ganga) | 1.20 | 🟢 Normal | -0.009 |  |
| 2026-06-24 22:08:28 | Badalgama (Maha Oya) | 2.62 | 🟢 Normal | -0.010 |  |
| 2026-06-24 18:00:37 | Weraganthota (Mahaweli Ganga) | -3.41 | 🟢 Normal | -0.010 |  |
| 2026-06-24 22:02:33 | Deraniyagala (Kelani Ganga) | 0.96 | 🟢 Normal | -0.010 |  |
| 2026-06-24 22:06:35 | Holombuwa (Kelani Ganga) | 0.71 | 🟢 Normal | -0.010 |  |
| 2026-06-24 22:03:12 | Norwood (Kelani Ganga) | 0.58 | 🟢 Normal | -0.010 |  |
| 2026-06-24 22:02:11 | Siyambalanduwa (Heda Oya) | 0.37 | 🟢 Normal | -0.010 |  |
| 2026-06-24 22:01:19 | Thalgahagoda (Nilwala Ganga) | 0.40 | 🟢 Normal | -0.011 |  |
| 2026-06-24 22:02:40 | Giriulla (Maha Oya) | 1.34 | 🟢 Normal | -0.011 |  |
| 2026-06-24 22:07:30 | Panadugama (Nilwala Ganga) | 2.75 | 🟢 Normal | -0.012 |  |
| 2026-06-24 22:01:16 | Magura (Kalu Ganga) | 2.00 | 🟢 Normal | -0.013 |  |
| 2026-06-24 22:03:36 | Rathnapura (Kalu Ganga) | 1.47 | 🟢 Normal | -0.019 |  |
| 2026-06-24 22:06:16 | Kalawellawa (Millakanda) (Kalu Ganga) | 4.58 | 🟢 Normal | -0.032 |  |
| 2026-06-24 22:08:59 | Putupaula (Kalu Ganga) | 1.55 | 🟢 Normal | -0.046 |  |
| 2026-06-24 22:02:19 | Hanwella (Kelani Ganga) | 2.35 | 🟢 Normal | -0.050 |  |
| 2026-06-24 22:02:51 | Kithulgala (Kelani Ganga) | 1.68 | 🟢 Normal | -0.121 |  |
| 2026-06-24 22:11:42 | Dunamale (Aththanagalu Oya) | 2.12 | 🟢 Normal | -0.146 |  |

## River Water Level Charts by Station

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

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)